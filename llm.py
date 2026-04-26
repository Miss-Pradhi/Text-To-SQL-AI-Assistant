from groq import Groq
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini = genai.GenerativeModel("gemini-1.5-flash")

def ask_llm(prompt):

    # Primary API = Groq
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role":"user","content":prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content

    except:
        print("Groq failed, switching to Gemini")

    # Fallback API
    try:
        response = gemini.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Both APIs failed: {str(e)}"