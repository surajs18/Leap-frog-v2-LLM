from tools.chat_ollama import query_mistral

def run_performance_module():
    with open("prompts/performance_prompt.txt", "r") as f:
        prompt = f.read()

    print("\n📌 Running: PERFORMANCE & RESULTS\n")
    response = query_mistral(prompt)
    print(response)
