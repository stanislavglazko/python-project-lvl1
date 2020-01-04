import random


def prime(a):
    divider = 2
    while a % divider != 0:
        divider += 1
    if divider == a:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def make_round():
    random_number = random.randint(1, 100)
    correct_answer = prime(random_number)
    return random_number, correct_answer


def rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    make_round()
    rules()


if __name__ == '__main__':
    main()
