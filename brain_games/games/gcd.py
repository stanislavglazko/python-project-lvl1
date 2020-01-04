import random


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return str(a + b)


def make_round():
    random1 = random.randint(1, 100)
    random2 = random.randint(1, 100)
    random_number = str(random1) + " " + str(random2)
    correct_answer = gcd(random1, random2)
    return random_number, correct_answer


def rules():
    return 'Find the greatest common divisor of given numbers.'


def main():
    make_round()
    rules()
