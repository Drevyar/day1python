import random

def test_random():
    random_number = random.randint(1, 100)
    print(random_number)

guess_number = int(input('Enter guess number ( 1 - 100 ): '))

    
test_random()