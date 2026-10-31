# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game

# List of questions
questions = [
    "What is the capital of France?",
    "Who is known as the Father of the Indian Constitution?",
    "Which planet is known as the Red Planet?",
    "What is the largest ocean in the world?",
    "Who invented the telephone?",
    "Which gas is most abundant in Earth’s atmosphere?",
    "What is the national animal of India?",
    "Which country gifted the Statue of Liberty to the USA?",
    "What is the smallest prime number?",
    "Which organ purifies blood in the human body?"
]

# List of options (correct answer is always the last element)
options = [
    ["Berlin", "Madrid", "Paris", "Rome", "Paris"],
    ["Mahatma Gandhi", "Jawaharlal Nehru", "B. R. Ambedkar", "Sardar Patel", "B. R. Ambedkar"],
    ["Venus", "Mars", "Jupiter", "Saturn", "Mars"],
    ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", "Pacific Ocean"],
    ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Marconi", "Alexander Graham Bell"],
    ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", "Nitrogen"],
    ["Lion", "Elephant", "Tiger", "Leopard", "Tiger"],
    ["Germany", "France", "England", "Italy", "France"],
    ["0", "1", "2", "3", "2"],
    ["Heart", "Lungs", "Liver", "Kidneys", "Kidneys"]
]

# Prize money for each question
prize_money = [1000, 2000, 3000, 5000, 10000,
               20000, 40000, 80000, 160000, 320000]

amount_won = 0

for i in range(len(questions)):
    print(f"\nQuestion {i+1}: {questions[i]}\n")

    # Display options (only first 4)
    print("A.", options[i][0])
    print("B.", options[i][1])
    print("C.", options[i][2])
    print("D.", options[i][3])

    answer = input("\nEnter your answer (A/B/C/D): ").upper()

    # Map user choice to option value
    if answer == "A":
        user_ans = options[i][0]
    elif answer == "B":
        user_ans = options[i][1]
    elif answer == "C":
        user_ans = options[i][2]
    elif answer == "D":
        user_ans = options[i][3]
    else:
        print("Invalid choice ❌")
        break

    # Check answer (correct answer is last element)
    if user_ans == options[i][-1]:
        amount_won = prize_money[i]
        print(f"Correct Answer ✅ You won ₹{amount_won}")
    else:
        print("Wrong Answer ❌")
        break

# Final amount
print("\n🏆 Game Over")
print(f"You are taking home ₹{amount_won}")

