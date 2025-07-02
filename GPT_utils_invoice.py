import requests
import os
from config import api_key

api_key = os.getenv("OPENAI_API_KEY") or api_key

def generate_invoice_summary(details):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You generate concise, professional invoice summaries."},
            {"role": "user", "content": f"Write a short summary for this invoice:\n{details}"}
        ],
        "max_tokens": 100
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"❌ AI Error: {e}")
        return "AI could not generate summary."
