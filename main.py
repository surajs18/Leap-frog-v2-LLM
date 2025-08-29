from themes import motivation_energy, confidence, performance, mindset

def main():
    print("Welcome to the AI Self-Improvement Assistant\n")
    print("Choose a theme to work on:")
    print("1. Motivation & Energy")
    print("2. Confidence & Imposter Syndrome")
    print("3. Performance & Results")
    print("4. Mindset")
    
    choice = input("\nEnter the number: ")

    if choice == "1":
        motivation_energy.run_energy_module()
    elif choice == "2":
        confidence.run_confidence_module()
    elif choice == "3":
        performance.run_performance_module()
    elif choice == "4":
        mindset.run_mindset_module()
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
