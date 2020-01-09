import random
import operator


def make_round():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    r = (('+', operator.add),
         ('-', operator.sub),
         ('*', operator.mul))
    our_operator, our_operation = random.choice(r)
    correct_answer = our_operation(first, second)
    random_number = '{} {} {} '.format(first, our_operator, second)
    return random_number, correct_answer


def rules():
    return 'What is the result of the expression?'
