import random
import operator


def make_round():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    r = (('+', operator.add(first, second)),
         ('-', operator.sub(first, second)),
         ('*', operator.mul(first, second)))
    operation = random.choice(r)
    correct_answer = str(operation[1])
    random_number = '{} {} {} '.format(first, operation[0], second)
    return random_number, correct_answer


def rules():
    return 'What is the result of the expression?'


def main():
    make_round()
    rules()


if __name__ == '__main__':
    main()
