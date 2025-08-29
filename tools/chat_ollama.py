import requests

def query_mistral(prompt, model="mistral"):
    url = "http://localhost:11434/api/generate"
    response = requests.post(url, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    return response.json().get("response", "")
