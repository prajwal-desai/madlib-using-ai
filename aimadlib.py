
import google.generativeai as genai  
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API key not found! Make sure to set it in the .env file.")


genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Getting user inputs
noun1 = input("Enter a noun: ")
adjective1 = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb: ")

# AI Prompt
prompt = f"""
Create a short, funny story using these words:
- Noun: {noun1}
- Adjective: {adjective1}
- Verb: {verb1}
- Noun: {noun2}
- Verb: {verb2}

Make the story engaging, and unique!
"""


response = model.generate_content(prompt)


print("\n Here’s Your AI-Generated Story: \n")
print(response.text)
