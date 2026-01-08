import os
import openai
from dotenv import load_dotenv

# 1. Load your .env file
load_dotenv()

# 2. Get the value of the label "GEMINI_API_KEY" from your .env
# We use the LABEL name, not the actual key value here
API_KEY = os.getenv("AIzaSyAGrFJje3ulKbDbt68TaijktAf7TA09J6g")

# 3. Backup: If .env fails to load, use the key directly
if not API_KEY:
    API_KEY = "AIzaSyAGrFJje3ulKbDbt68TaijktAf7TA09J6g"

# 4. Initialize the client with the SPECIFIC Google OpenAI-compatible path
# Adding "/v1beta/openai/" to the end is required to stop the 404 error
client = openai.OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def call_gemini(messages):
    try:
        # Use the standard model name supported by the v1beta endpoint
        response = client.chat.completions.create(
            model="gemini-3-flash-preview", 
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        # If any other error happens, this will show us exactly what it is
        return f"Error: {e}"
    