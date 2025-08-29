from tools.chat_ollama import query_mistral
from tools.file_reader import read_file

def run_performance_module():
    qna = read_file("history/performance_qna.txt")
    prompt = read_file("prompts/performance_understanding.txt")
    full_prompt = f"User interaction:\n {qna}\n\n{prompt}"

    print("\n📌 Running: UNDERSTAND PERFORMANCE & RESULTS\n")
    response = query_mistral(full_prompt)
    print(response)

def ask_performance_question():
    question = read_file("prompts/performance_question_generate.txt")

    print("\n📌 PERFORMANCE & RESULTS QUESTIONS\n")
    response = query_mistral(question)
    print(response)
