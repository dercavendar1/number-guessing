import math
import random

# set initial conditions with minimum and maximum values for the random number
min_num = random.randint(1, 10000)
max_num = random.randint((min_num + 10), 10100)
generated_number = random.randint(min_num, max_num)
guess = 0
attempts = 1  # sets number of tries at 1 initially

# provide initial hint for the random number either over or under half of max_num
print(f'Guess a number between {min_num} and {max_num}')
if (generated_number >= math.floor((((max_num - min_num)) / 2) + min_num)):
    print(
        f'the number is between {math.floor((((max_num - min_num)) / 2) + min_num)} and {max_num}')
else:
    print(
        f'the number is between {min_num} and {math.floor((((max_num - min_num)) / 2) + min_num)}')

# initial attempt at guessing
while guess == 0:
    try:
        guess = int(input('what is your guess at the number? '))
    except ValueError:
        print("Please only enter whole numbers. Please try again")

# loop to allow you to keep guessing until success
while (guess != generated_number):
    print(
        f'You were off by {abs(guess - generated_number)}, try again')
    try:
        guess = int(input('what is your guess at the number? '))
    except ValueError:
        print("Please only enter whole numbers. Please try again")
    attempts += 1  # increments number of tries to keep score

# success message
print(f'You Got the Number! It took you {attempts} tries')
