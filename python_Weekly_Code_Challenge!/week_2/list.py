"""
Write a program that accepts user input to create a list of integers. 
Then, compute the sum of all the integers in the list.
"""
   
# Get numbers from user
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

# Calculate and print sum
print("Sum:", sum(numbers))