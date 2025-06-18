import os
from openai import OpenAI

api_key = os.getenv("API_KEY")

client = OpenAI(api_key=api_key)