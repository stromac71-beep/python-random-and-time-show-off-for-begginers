import random
import time
x = random.random()
x = x * 10000000
x = int(x)
while x > 10000:
    x = x - 1
    z = random.random()
    x = x * z
    x = int(x)
number_error = False
y = int(input("enter a number between 0 and 1000: "))
if y > 10000:
    print("error code[1], number is over 10000. please enter a valid number")
    number_error = True
    time.sleep(7)
    print("")
if y < 0:
    print("error code[2], number is less then 0. please enter a valid number")
    number_error = True
    time.sleep(7)
    print("")
while number_error == False and x < y:
    x = x + 1
while number_error == False and x > y:
    x = x - 1
if x == y:
    print(f"your number is {y}, we guess {x}")
