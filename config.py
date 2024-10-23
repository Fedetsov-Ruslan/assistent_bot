import os
from dotenv import load_dotenv

load_dotenv()

AI_TOKEN = os.getenv("AI_TOKEN")
SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")