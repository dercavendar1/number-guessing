import math
import random

# set initial conditions with minimum and maximum values for the random number
min_num = random.randint(1, 10000)
# generates a random max number that will be at least 10 greater than min_num
max_num = random.randint((min_num + 10), 10100)
# generates the random number to be guessed
generated_number = random.randint(min_num, max_num)
# initialize guess variable to prevent infinite loop
guess = 0
# sets number of tries at 1 initially
attempts = 1

# provide initial hint for the random number either over or under half of max_num
print(f'Guess a number between {min_num} and {max_num}')
# print this if generated_number is greater than half way between the range
if (generated_number >= math.floor((((max_num - min_num)) / 2) + min_num)):
    print(
        f'the number is between {math.floor((((max_num - min_num)) / 2) + min_num)} and {max_num}')
# print this if generated_number is less than half way between the range
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
        attempts += 1  # increments number of tries to keep score
    except ValueError:
        print("Please only enter whole numbers. Please try again")


# success message
print(f'You Got the Number! It took you {attempts} tries')
