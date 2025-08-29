from tools.chat_ollama import query_mistral, query_ollama
from tools.file_reader import read_file

def run_mindset_module():
    qna = read_file("history/mindset_qna.txt")
    prompt = read_file("prompts/mindset_understanding.txt")
    full_prompt = f"User interaction:\n {qna}\n\n{prompt}"

    # print(f"\n📌 Running: UNDERSTAND MINDSET\n {full_prompt} \n\n")
    print("\n📌 Running: UNDERSTAND MINDSET\n")
    response = query_mistral(full_prompt)
    print(response)

def ask_mindset_question():
    question = read_file("prompts/mindset_question_generate.txt")

    print("\n📌 MINDSET QUESTION\n")
    response = query_ollama(question)#query_mistral(question)
    print(response)