from tools.chat_ollama import query_mistral
from tools.file_reader import read_file

def run_motivation_energy_module():
    qna = read_file("history/motivation_qna.txt")
    prompt = read_file("prompts/motivation_understanding.txt")
    full_prompt = f"User interaction:\n {qna}\n\n{prompt}"

    print("\n📌 Running: UNDERSTAND MOTIVATION & ENERGY\n")
    response = query_mistral(full_prompt)
    print(response)

def ask_motivation_energy_question():
    question = read_file("prompts/motivation_question_generate.txt")

    print("\n📌 MOTIVATION & ENERGY QUESTIONS\n")
    response = query_mistral(question)
    print(response)
