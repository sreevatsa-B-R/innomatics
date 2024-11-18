import streamlit as st
import google.generativeai as genai

f = open("key.txt")
key = f.read()

genai.configure(api_key=key)

st.title("💬 An AI :blue[Code Reviewer]")

system_prompt = """
You are an AI Code Reviewer. When given Python code, you need to:
Heading should be Code Review
1. Heading as Bug Report - Review the code and provide a bug report if any are present in points.
2. Heading as Fixed Code - Provide the fixed version of the code without any bugs.
If given any non-Python code or irrelevant content, politely decline to answer.

Over all you should analyze the submitted code and identify potential bugs, errors, or areas of improvement and should also provide the fixed code snippets.
"""

user_prompt = st.text_area(":blue[Enter Your Python Code]:", placeholder="Type Your Code...")
btn_click = st.button("Generate Code")

model = genai.GenerativeModel(model_name="gemini-1.5-pro", 
                              system_instruction=system_prompt)

if btn_click==True:
    response = model.generate_content(user_prompt)
    st.write(response.text)