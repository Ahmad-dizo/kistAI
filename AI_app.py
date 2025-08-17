
import streamlit as st
import cohere
import os

API_key = "WkiTWSGbtHjxWhXyeUXMYFxr9olmfVLLMDY9r2An"
co = cohere.Client(API_key)

def generate_response(concept, role):
    '''This function takes as input an AI concept and an audience role, makes a prompt for the language model to explain the concept to the correct audience, prompt the LLM and returns the LLM response '''
    PROMPT = f"Concisely explain the AI concept {concept} to someone with the experience of a {role} in the field of artificial intelligence. Do not give an answer if the concept is not related to AI."
    response = co.chat(message=PROMPT)
    return response.text

st.title("🤖 Learning AI 🤖")
form = st.form(key="user_settings")
with form:
    AI_concept = st.text_input("Enter the AI concept you are interested in:", key = "AI_concept")
    role = st.selectbox("For what audience would you like it to be explained?",
                          ("Expert", 
                           "Layman", "12 year old child"),)
    generate_button = form.form_submit_button("Explain AI concept")
    if generate_button:
        with st.spinner('Wait for it...'): #add a waiting icon while waiting for the response
            response = generate_response(AI_concept, role)
        st.write(response)

col1, col2 = st.columns(2)


st.write("\n\n\nData Science and AI Training 2025")
st.write("KARUME INSITUTE OF SCIENCE AND TECHNOLOGY")
st.write("Programed by AHMAD HAJI and ALI MAKAME")
st.image("kist logo.jpg", width = 300)
