import openai
import os
from dotenv import load_dotenv
# from pathlib import Path


load_dotenv()


openai.api_key = os.getenv('KEY')

# print("api key " + openai.api_key)
