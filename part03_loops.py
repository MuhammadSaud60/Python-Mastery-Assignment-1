"""
    Name: Muhammad Saud
    Cohort: PSEB-AI-PEW-01 (PSEB-AI-PEW-01)

"""




# Warm-up: 

number = int(input('Enter a number: '))

for i in range(1, 11):

    print(f'{number} * {i}: {number * i}')



# Build: ATM PIN Check

PIN = '4321'

TRIES = 3

while TRIES > 0:
    user_pin = input('Enter Your Pin: ')
    TRIES -= 1

    if user_pin == PIN:
        print('WELCOME')
        break

    elif user_pin != PIN:
        print(f'Wrong Password, LEFT {TRIES}')

    
    if TRIES == 0:
        print('Card Blocked')
        

# Challenge: Number guessing game

import random

SECRET_NUMBER = random.randint(1, 50)
PLAY = True
count_guesses = 0

while PLAY:
    try:
        user_guess = int(input('Guess the number: '))
    except ValueError as e:
        print('Invalid input, only whole number is acceptable')
        continue
    
    count_guesses += 1

    if user_guess == SECRET_NUMBER:
        print(f'GOT IT IN {count_guesses} GUESSES')
        play = input('PLAY AGAIN? (Y/N)')

        if play.lower() == 'y':
            SECRET_NUMBER = random.randint(1,50)
            count_guesses = 0
            PLAY = True

        else: 
            PLAY = False


    elif user_guess > SECRET_NUMBER:
        print('TOO HIGH')

    else:
        print('TOO LOW')



# Star Triangle

LIMIT = 5

for i in range(1, LIMIT + 1):
    for j in range(i):
        print("*", end=' ')

    print(" ")


# EVEN SUM (1 TO 100)

total = 0

for i in range(1, 101):

    if i % 2 == 0:
        total += i

print(total)