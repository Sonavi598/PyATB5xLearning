# Task 1 for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 -> num1
# 2 -> num2
# Q -> 7
# R -> 1
#from argparse import REMAINDER

num_1 = int(input("Enter a Value of num1: "))
num_2 = int(input("Enter a Value of num2: "))

Quotient = num_1 // num_2
print(f"Quotient of given equation is: {Quotient}")

REMAINDER = num_1 % num_2
print(f"Remainder of given equation is: {REMAINDER}")

