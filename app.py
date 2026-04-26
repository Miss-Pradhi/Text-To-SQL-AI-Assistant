import streamlit as st
import pandas as pd
from db import init_db
from chain import run_pipeline
from dashboard import show_dashboard
from rag import build_vectorstore


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI SQL Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Text-to-SQL Assistant")
st.caption("Ask questions in plain English and get SQL results instantly.")

# -----------------------------
# Initialize DB
# -----------------------------
init_db()

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("⚡ Quick Questions")

    st.write("Try these examples:")

    st.code("Show all customers")
    st.code("Show all sales")
    st.code("Total sales amount")
    st.code("Top 5 products by sales")
    st.code("Customers from Pune")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# User Input
# -----------------------------
query = st.chat_input("Ask your database question...")

if query:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    with st.spinner("Thinking..."):

        sql, result = run_pipeline(query)

        st.session_state.messages.append({
            "role": "assistant",
            "sql": sql,
            "result": result
        })

# -----------------------------
# Display Chat Messages
# -----------------------------
for msg in st.session_state.messages:

    # USER MESSAGE
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])

    # ASSISTANT MESSAGE
    else:
        with st.chat_message("assistant"):

            st.subheader("📝 Generated SQL")
            st.code(msg["sql"], language="sql")

            st.subheader("📊 Result")

            result = msg["result"]

            # If error string
            if isinstance(result, str):
                st.error(result)

            else:
                if result:

                    # Detect columns automatically
                    if len(result[0]) == 3:
                        df = pd.DataFrame(
                            result,
                            columns=["ID", "Name", "City"]
                        )

                    elif len(result[0]) == 5:
                        df = pd.DataFrame(
                            result,
                            columns=[
                                "ID",
                                "Product",
                                "Region",
                                "Amount",
                                "Customer_ID"
                            ]
                        )

                    elif len(result[0]) == 2:
                        df = pd.DataFrame(
                            result,
                            columns=["Category", "Value"]
                        )

                    else:
                        df = pd.DataFrame(result)

                    st.dataframe(
                        df,
                        use_container_width=True,
                        hide_index=True
                    )

                    # -----------------------------
                    # Charts
                    # -----------------------------
                    chart = show_dashboard(result)

                    if chart:
                        _, fig = chart
                        st.subheader("📈 Chart")
                        st.plotly_chart(
                            fig,
                            use_container_width=True
                        )

                else:
                    st.info("No records found.")