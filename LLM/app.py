import streamlit as st
from llama_cpp import Llama

# Load the model
llm = Llama(model_path="/Users/apple/models/phi-2.Q4_K_M.gguf")

# Function to generate response
def get_response(condition):
    explanation_prompt = f"Explain {condition} in simple terms."
    coping_prompt = f"Suggest coping strategies for {condition}."
    
    try:
        explanation = llm(explanation_prompt)['choices'][0]['text'].strip()
        coping = llm(coping_prompt)['choices'][0]['text'].strip()
        return explanation, coping
    except Exception as e:
        return f"Error while processing the request: {str(e)}", ""

# Streamlit UI
st.title("🩺 AI Mental Health Chatbot")

condition = st.text_input("Enter the mental health condition:")

if st.button("Get Explanation & Coping Strategies"):
    if condition.strip() == "":
        st.error("Please enter a valid mental health condition.")
    else:
        explanation, coping_mechanisms = get_response(condition)
        st.subheader("🧠 Explanation")
        st.write(explanation if explanation else "No explanation found.")
        
        st.subheader("💡 Coping Strategies")
        st.write(coping_mechanisms if coping_mechanisms else "No coping strategies found.")
