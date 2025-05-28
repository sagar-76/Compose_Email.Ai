import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama3-70b-8192"
)

st.set_page_config(page_title="AI Email Generator")
st.title("Email Generator using LLaMA 3 (Groq + LangChain)")

user_prompt = st.text_area("Enter what the email should be about")
user_name = st.text_input("Enter your name", value="Sagar Bhagwani")
receiver_name = st.text_input("Enter the receiver's name", value="John")

if st.button("Generate Email"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating email..."):

            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are an expert email writer. Respond with only the email content. If names are needed, use [Receiver's Name] and [Your Name]."),
                ("human", "{user_input}")
            ])

            chain = prompt | llm
            response = chain.invoke({"user_input": user_prompt})

            email_text = response.content
            email_text = email_text.replace("[Your Name]", user_name)
            email_text = email_text.replace("[Receiver's Name]", receiver_name)

            st.subheader("📨 Generated Email:")
            st.write(email_text)
