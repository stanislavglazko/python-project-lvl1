import random


def is_prime(a):
    divider = 2
    while a % divider != 0:
        divider += 1
    return divider == a


def make_round():
    random_number = random.randint(1, 100)
    correct_answer = "yes" if is_prime(random_number) else "no"
    return random_number, correct_answer


def rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
