#Task 1: Check if a Number is Even or Odd
#Problem Statement:  Write a Python program that:
#1. 	Takes an integer input from the user.
#2. 	Checks whether the number is even or odd using an if-else statement.
#3. 	Displays the result accordingly.
a=int(input("Enter Your number:"))
if (a%2==0):
    print(a, "is an even")
else:
    print(a,"is an odd")

print("thanku")

#Task 2: Sum of Integers from 1 to 50 Using a Loop
 
#Problem Statement: Write a Python program that:
#1.   Uses a for loop to iterate over numbers from 1 to 50.
#2.   Calculates the sum of all integers in this range.
#3.   Displays the final sum.
n=1
for i in range(0,51):
    n=n+i
if i==50:
    print("the sum of number from 1 to 50 is:" ,n)