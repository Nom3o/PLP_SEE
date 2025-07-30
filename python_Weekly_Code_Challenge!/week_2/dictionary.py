"""
Write a program that uses a dictionary to store information about a person,
such as their name, age, and favorite color.
Ask the user for input and store the information in the dictionary.
Then, print the dictionary to the console.
"""

user_data = {}

user_data['name'] = input('What is your name?: ')
user_data['age'] = int(input('How old are you?: '))
user_data['color'] = input('What is your favorite color?: ')

print(user_data)
