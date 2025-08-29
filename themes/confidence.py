from tools.chat_ollama import query_mistral
from tools.file_reader import read_file

def run_confidence_module():
    qna = read_file("history/confidence_qna.txt")
    prompt = read_file("prompts/confidence_understanding.txt")
    full_prompt = f"User interaction:\n {qna}\n\n{prompt}"

    print("\n📌 Running: UNDERSTAND CONFIDENCE & IMPOSTER SYNDROME\n")
    response = query_mistral(full_prompt)
    print(response)

def ask_confidence_question():
    question = read_file("prompts/confidence_question_generate.txt")

    print("\n📌 CONFIDENCE & IMPOSTER SYNDROME QUESTIONS\n")
    response = query_mistral(question)
    print(response)
