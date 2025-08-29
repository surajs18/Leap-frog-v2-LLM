from tools.chat_ollama import query_mistral

def run_mindset_module():
    with open("prompts/mindset_prompt.txt", "r") as f:
        prompt = f.read()

    print("\n📌 Running: MINDSET\n")
    response = query_mistral(prompt)
    print(response)
