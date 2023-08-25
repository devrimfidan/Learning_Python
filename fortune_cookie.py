import random

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,3)

fortune_text = ''

if fortune_number == 1:
    fortune_text = 'You will have a great Day!'

if fortune_number == 2:
    fortune_text = 'It will be tough... but worth it'

if fortune_number == 3:
    fortune_text = 'You will gt married this year!'

print(f'{fortune_text}  Your Lucky Number is: {lucky_number}')