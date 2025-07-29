"""

Simple Quiz Game 🎮
Create a multiple-choice quiz 
with questions about Python,
 movies, or any fun topic! 
 Display scores at the end and 
 allow the user to play again. 🏆


"""

import random

def run_quiz():
    print("````````````````````````````````````")
    print("Welcome to the Simple Quiz Game! 🎮")
    print("````````````````````````````````````\n")
    
    # Quiz questions with options and correct answers
    questions = [
        {
            "question": "Which Python keyword is used to define a function?",
            "options": ["A. def", "B. function", "C. define", "D. func"],
            "answer": "A"
        },
        {
            "question": "what is the out put of the code: print(200*2):_______",
            "options": ["A. 400", "B. 202", "C. 4000", "D. 800"],
            "answer": "A"
        },
        {
            "question": "Which of these is NOT a Python data type?",
            "options": ["A. list", "B. tuple", "C. array", "D. dictionary"],
            "answer": "C"
        },
        {
            "question": "What is the output of the following code: print(4**2)",
            "options": ["A. 8", "B. 16", "C. 20", "D. 6"],
            "answer": "B"
        },
        {
            "question": "What does the 'elif' keyword mean in Python?",
            "options": ["A. else if", "B. end if", "C. extended if", "D. exclusive if"],
            "answer": "A"
        },
        
    ]

    score = 0
    random.shuffle(questions)  # Shuffle questions for variety
    
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
        
        while True:
            user_answer = input("Your answer (A/B/C/D): ").upper()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            print("Invalid input! Please enter A, B, C, or D.")
        
        if user_answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")
    
    total_questions = len(questions)
    percentage = (score / total_questions) * 100
    
    print("\n📊 Quiz Results:")
    print(f"You got {score} out of {total_questions} questions correct!")
    print(f"That's {percentage:.1f}%!")
    
    if percentage == 100:
        print("🏆 Perfect score! You're amazing!")
    elif percentage >= 70:
        print("👍 Great job!")
    elif percentage >= 50:
        print("😊 Not bad!")
    else:
        print("🤔 Keep practicing!")
    
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again == 'yes':
        print("\n" + "="*50 + "\n")
        run_quiz()
    else:
        print("\nThanks for playing! Goodbye! 👋")

# Start the quiz
run_quiz()