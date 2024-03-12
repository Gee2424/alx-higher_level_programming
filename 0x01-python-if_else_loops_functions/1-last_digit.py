#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = number % 10
last = number % 10
if last > 5:
    str2 = ('and is greater than 5')
elif last == 0:
    str2 = ('and is 0')
elif last < 6 and last != 0:
    str2 = ('and is less than 6 and not 0')
print(f"Last digit of {number} is {str} {str2}.")
