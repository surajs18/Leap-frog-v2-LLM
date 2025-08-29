from themes import motivation_energy, confidence, performance, mindset

def main():
    print("Welcome to the AI Self-Improvement Assistant\n")
    print("Choose a theme to work on:")
    print("1. Generate questions on Motivation & Energy")
    print("2. Understand your status on Motivation & Energy")
    print("3. Generate questions on Confidence & Imposter Syndrome")
    print("4. Understand your status on Confidence & Imposter Syndrome")
    print("5. Generate questions on Performance & Results")
    print("6. Understand your status on Performance & Results")
    print("7. Generate questions on Mindset")
    print("8. Understand your status on Mindset")

    choice = input("\nEnter the number: ")

    if choice == "1":
        motivation_energy.ask_motivation_energy_question()
    elif choice == "2":
        motivation_energy.run_motivation_energy_module()
    elif choice == "3":
        confidence.ask_confidence_question()
    elif choice == "4":
        confidence.run_confidence_module()
    elif choice == "5":
        performance.ask_performance_question()
    elif choice == "6":
        performance.run_performance_module()
    elif choice == "7":
        mindset.run_mindset_module()
    elif choice == "8":
        mindset.run_mindset_module()
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
