import os
from dotenv import load_dotenv

# Load .env
load_dotenv(r"c:\Users\patel\OneDrive\Desktop\GovernmentSkim\MiroFish\backend\.env")

from openai import OpenAI
import json

api_key = os.getenv("LLM_API_KEY")
base_url = os.getenv("LLM_BASE_URL")
model = os.getenv("LLM_MODEL_NAME")

print(f"API_KEY: {api_key[:5]}...")
print(f"BASE_URL: {base_url}")
print(f"MODEL: {model}")

client = OpenAI(api_key=api_key, base_url=base_url)

try:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Return {\"hello\": \"world\"} as JSON"}],
        response_format={"type": "json_object"}
    )
    print("SUCCESS!")
    print(response.choices[0].message.content)
except Exception as e:
    print("ERROR:")
    import traceback
    traceback.print_exc()
