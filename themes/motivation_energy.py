from tools.chat_ollama import query_mistral

def run_energy_module():
    with open("prompts/motivation_prompt.txt", "r") as f:
        prompt = f.read()

    print("\n📌 Running: MOTIVATION & ENERGY\n")
    response = query_mistral(prompt)
    print(response)
