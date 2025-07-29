"""
Intro to Python Assignment
"""

print('___________________________')
print('| Basic Calculator Program |')
print('```````````````````````````')

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
operation = input('Enter a mathimatical operation: + , - , / or * : ')

if operation == '+':
    print('The addition is: ' , num1 + num2)
elif operation == '-':
    print('The subtraction is: ', num1 - num2)
elif operation == '*':
    print('The multiplication is: ', num1 * num2)
elif operation == '/':
    print('The division is: ', num1 / num2)
else:
    print('Please insert a valid input!!')

print('_____THE END______')
