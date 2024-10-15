# Program Name: Lab5.py
# Course: IT1114
# Student Name: Zenzele Broomfield
# Assignment Number: Lab5
# Due Date: 9/29/2024
# Purpose: prompt users to use a prime number for the starting and ending number
# Resources: IDLE(Python 3.12 64 bit)

def is_prime(num):
    if num == 1:
        return True
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# prompt for starting and ending numbers
start = int(input("Starting Number: "))
end = int(input("Ending Number: "))

# prime numbers in given range
for num in range(start, end + 1):
    if is_prime(num):
        print(num)
