#!/usr/bin/env python3

number = int(input("Enter the first number:\n"))
number_second = int(input("Enter the second number:\n"))
result = number * number_second

print(f"{number} x {number_second} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")