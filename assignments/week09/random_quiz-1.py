"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
import random

random_number = random.randint(1, 20)
print(random_number)

print('Guess my  number ( 1 - 20 ).')
print('You have only 6 6 attempts. ')

for i in range(1,7):
    try:
        guess_number = int(input(f'Attempt {i}/6 - Enter your guess: '))
        if guess_number <= 0:
            print('Number must more than 0.')
    except ValueError:
        print("Please enter a valid number.")
        continue


    if random_number == guess_number:
        print('Congalutation.')
        break
    elif random_number > guess_number:
        print(f'More than {guess_number}')
    else:
        print(f'Less than {guess_number}')

else:
    print(f'The correct number is {random_number}.')