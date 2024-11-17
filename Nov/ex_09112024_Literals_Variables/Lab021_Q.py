# Write a program to take 2 user input then sum the number
# mul -> *
# div -> /

# Logic Building
# step 1: i/p -> num1, num2 -> int or float?
#o/p -> sum - int ,sub - int, div - float

#step 2
# DAA: Don't assume anything (Ask user)
num1 = int(input("enter a number 1: "))
num2 = int(input("Enter a number 2: "))
print(type(num1))
print(type(num2))

print("Sum is: ",num1 + num2)
print("Sub is: ",num1 - num2)
print("Mul is: ",num1 * num2)
print("Div is: ",num1 / num2)




