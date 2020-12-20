import math
import random

# set initial conditions with minimum and maximum values for the random number
min_num = random.randint(1, 10000)
max_num = random.randint((min_num + 10), 10100)
generated_number = random.randint(min_num, max_num)
attempts = 1  # sets number of tries at 1 initially

# provide initial hint for the random number either over or under half of max_num
print(f'Guess a number between {min_num} and {max_num}')
# TODO: fix initial guess to be asscociated to the min and max not just max
if (generated_number >= math.floor(max_num / 2)):
    print(f'the number is greater than or equal to {math.floor(max_num / 2)}')
else:
    print(f'the number is less than {math.floor(max_num / 2)}')

# initial attempt at guessing
# TODO: sanitize input to only allow int inputs with try catch block
guess = int(input('what is your guess at the number? '))

# loop to allow you to keep guessing until success
while (guess != generated_number):
    print(
        f'You were off by {abs(guess - generated_number)}, try again')
    guess = int(input('what is your guess at the number? '))
    attempts += 1  # increments number of tries to keep score

# success message
print(f'You Got the Number! It took you {attempts} tries')
