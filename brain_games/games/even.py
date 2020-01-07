import random


def make_round():
    random_number = random.randint(1, 100)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer


def rules():
    return 'Answer "yes" if number even otherwise answer "no".'
