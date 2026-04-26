from rag import retrieve_context
from llm import ask_llm
from db import engine
from sqlalchemy import text
import re


# -----------------------------
# Clean SQL returned by LLM
# -----------------------------
def clean_sql(sql):
    if not sql:
        return ""

    # Remove markdown code blocks
    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)

    # Remove backticks
    sql = sql.replace("`", "")

    # Remove extra spaces
    sql = sql.strip()

    return sql


# -----------------------------
# Block dangerous SQL
# -----------------------------
def is_safe_sql(sql):
    blocked = ["drop", "delete", "truncate", "update", "alter"]

    lower_sql = sql.lower()

    for word in blocked:
        if word in lower_sql:
            return False

    return True


# -----------------------------
# Ask model to fix broken SQL
# -----------------------------
def fix_sql(sql, error):
    prompt = f"""
You are an expert SQLite developer.

Fix this SQL query for SQLite.

Return ONLY corrected SQL.

Wrong Query:
{sql}

Error:
{error}
"""

    fixed = ask_llm(prompt)
    return clean_sql(fixed)


# -----------------------------
# Main Pipeline with RAG
# -----------------------------
def run_pipeline(user_query):

    # Retrieve relevant context from vector DB
    context = retrieve_context(user_query)

    prompt = f"""
You are an expert SQLite SQL generator.

Use the following retrieved knowledge to answer accurately.

Retrieved Context:
{context}

Database Tables:

customers(
id INTEGER,
name TEXT,
city TEXT
)

sales(
id INTEGER,
product TEXT,
region TEXT,
amount INTEGER,
customer_id INTEGER
)

Rules:
1. Return ONLY SQL query
2. Use valid SQLite syntax
3. Use JOIN when customer/city needed
4. No explanation
5. No markdown

User Query:
{user_query}
"""

    # Generate SQL
    sql = clean_sql(ask_llm(prompt))

    # Safety check
    if not is_safe_sql(sql):
        return sql, "Dangerous query blocked."

    # First attempt
    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql)).fetchall()

        return sql, result

    except Exception as e:

        # Self-healing retry
        fixed_sql = fix_sql(sql, str(e))

        if not is_safe_sql(fixed_sql):
            return fixed_sql, "Dangerous query blocked."

        try:
            with engine.connect() as conn:
                result = conn.execute(text(fixed_sql)).fetchall()

            return fixed_sql, result

        except Exception as e2:
            return fixed_sql, f"Error: {str(e2)}"