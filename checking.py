from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env from current directory

print("GROQ_API_KEY from env:", os.getenv("GROQ_API_KEY"))  # Check if key loads
