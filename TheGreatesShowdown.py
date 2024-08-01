# The Greatest Showdown 
# Task 1:  Identify the Greatest: Write a Python program that asks the user to enter three numbers. 
#          Your code should then identify and print out the largest number among the three.

# Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.



number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

if (number1 >= number2) and (number1 >= number3):
    largest = number1
elif (number2 >= number1) and (number2 >= number3):
    largest = number2
else:
    largest = number3

if (number1 <= number2) and (number1 <= number3):
    smallest = number1
elif (number2 <= number1) and (number2 <= number3):
    smallest = number2
else:
    smallest = number3


print("The largest number is" , largest) 
print("The smallest number is" , smallest)