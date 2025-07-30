"""
Write a program that accepts user input to create two sets of integers.
Then, create a new set that contains 
only the elements that are common to both sets.
"""


print('Use space between the numbers!')
set1 = set(input('Enter the first set of numbers: ').split())
set2= set(input('Enter the set set of numbers: ').split())
print('The common numbers are: ', set1 & set2)