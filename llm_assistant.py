import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

#Load the Google API Key from .env file
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("Missing GOOGLE_API_KEY environment variable. Please define it in your .env file.")

#Initialize the Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=google_api_key,
    temperature=0.3
)

#Read the schema summary file
with open("schema_summary.txt", "r", encoding="utf-8") as f:
    schema_summary = f.read()

#Define prompt template for LangChain
prompt_template = PromptTemplate(
    input_variables=["schema_summary", "question"],
    template="""
You are an expert SQL developer working with a PostgreSQL database in the healthcare domain.
Below is a summary of the available tables and their structure:

{schema_summary}

Using only the information above, answer the following question by generating a valid PostgreSQL query.
Only return the SQL code. Do not include explanations or comments.

Question: {question}

SQL Query:
"""
)

#Create LangChain LLMChain
chain = LLMChain(llm=llm, prompt=prompt_template)

#Interactive console loop
print("Data model assistant activated. Type your question or 'exit' to quit.")
while True:
    user_input = input("Your question: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Shutting down assistant.")
        break

    response = chain.run(schema_summary=schema_summary, question=user_input)
    print("Answer:", response)
    print("\n")
