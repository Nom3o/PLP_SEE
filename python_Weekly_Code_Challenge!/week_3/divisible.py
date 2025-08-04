"""
Create a function called divisible_by_ten()
that has one parameter named num.

The function should return True if num is divisible by 10,
and False otherwise. Consider using modulo 
operator % to check for divisibility.

"""

num = int(input('Enter a number: '))
def divisible_by_ten():
    if num % 10 == 0:
        print('true')
    else:
        print('false')
        
divisible_by_ten()