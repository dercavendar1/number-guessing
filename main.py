import math
import random

min_num = 1
max_num = 100
generated_number = random.randint(min_num, max_num)

if (generated_number >= math.floor(max_num / 2)):
    print(f'the number is greater than or equal to {math.floor(max_num / 2)}')
else:
    print(f'the number is less than {math.floor(max_num / 2)}')

guess = int(input('what is your guess at the number? '))
print(
    f'The number was {generated_number} you were off by {abs(guess - generated_number)}')
