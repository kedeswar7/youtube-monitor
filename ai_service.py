import requests
import os

HF_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
HF_API_KEY = os.getenv("HF_API_KEY")

HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"} if HF_API_KEY else {}

def analyze_video(text, prompts):
    responses = {}
    for p in prompts:
        payload = {"inputs": f"{p}\n\n{text[:2000]}"}
        r = requests.post(HF_API_URL, headers=HEADERS, json=payload)
        data = r.json()
        if isinstance(data, list):
            responses[p] = data[0]["summary_text"]
        else:
            responses[p] = "AI response not available"
    return responses