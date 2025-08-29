from tools.chat_ollama import query_mistral

def run_confidence_module():
    with open("prompts/confidence_prompt.txt", "r") as f:
        prompt = f.read()

    print("\n📌 Running: CONFIDENCE & IMPOSTER SYNDROME\n")
    response = query_mistral(prompt)
    print(response)
