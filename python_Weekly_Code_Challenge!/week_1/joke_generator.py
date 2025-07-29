"""
Random Joke Generator 🤣
Build a program that stores a list of jokes 
and randomly selects one to display every time the user runs it.
Add a fun twist with jokes about Python or programming! 🐍💡

"""
import random

print('___________________________')
print('| Random Joke Generator 🤣 |')
print('```````````````````````````')

def python_jokes():
    jokes = [
        {
            "joke": "Why did the programmer quite his job?",
            "punchline": "Because he didn't get arrays! 🤣"
        },
        {
            "joke": "Why do Java programmers wear glasses?",
            "punchline": "Because they can't C#! 👓"
        },
        {
            "joke": "What do you call a programmer from Finland?",
            "punchline": "Nerdic! ❄️"
        },
        {
            "joke": "Why don't programmers like nature?",
            "punchline": "It has too many bugs! 🐛"
        },
        {
            "joke": "What's the object-oriented way to become wealthy?",
            "punchline": "Inheritance! 💰"
        },
        {
            "joke": "Why did the Python data scientist get arrested?",
            "punchline": "Because they got caught importing pandas! 🐼"
        },
        {
            "joke": "What's a programmer's favorite hangout place?",
            "punchline": "The Foo Bar! 🍻"
        },
        {
            "joke": "Why don't programmers like to go outside?",
            "punchline": "The sunlight causes syntax errors! ☀️"
        }
    ]

    joker = random.choice(jokes)
    
    print("\n" + "_"*20)
    print("Random joke:")
    print( "`"*20)

    print(joker["joke"])
    input("\n(press Enter for the punchline...)")
    print("\n" + joker["punchline"])
    print("\n" + "_"*40 + "\n")
    while True:
        another = input("\nWant to hear another joke? (yes/no): ").lower()
        if another in ["yes", "no"]:
            break
        print("Please enter 'yes' or 'no'")
    
    if another == "yes":
        python_jokes()
    else:
        print("\nThanks for laughing! Come back for more jokes later! 😄\n")
python_jokes()