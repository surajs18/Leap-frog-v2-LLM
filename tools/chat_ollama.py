import requests
import ollama, os

def query_mistral(prompt, model="mistral"):
    url = "http://localhost:11434/api/generate"
    response = requests.post(url, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    return response.json().get("response", "")

def query_ollama(prompt, model="mistral"):
    os.environ["OLLAMA_API_URL"] = "http://localhost:11434"
    response = ollama.generate(
    model=model,
    prompt=prompt,
    stream=False,

    )
    return response