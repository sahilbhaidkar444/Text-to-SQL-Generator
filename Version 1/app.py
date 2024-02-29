from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

load_dotenv()  # load all the environment variables

# configure google API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and provide sql query as a response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the sql database.
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()

        return rows
    except Exception as e:
        return str(e)

# Define your prompt:
prompt = [
    """
    Please enter your prompt here. 
"""
]


# Streamlit App
st.set_page_config(page_title="GeminiQuery Hub")
st.header("Gemini app for text to SQL")
question = st.text_input("Enter your question here regarding the anime database : ", key="input")
submit = st.button("Ask your question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("The Generated SQL Query:")
    st.code(response, language='sql')  # Display the SQL query with syntax highlighting
    print(response)
    data = read_sql_query(response, "anime.db")
    st.subheader("The Response is : ")
    for row in data :
        print(row)
        st.subheader(row)
