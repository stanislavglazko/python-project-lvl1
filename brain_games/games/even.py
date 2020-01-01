def make_round():
    import random
    rules = 'Answer "yes" if number even otherwise answer "no".'
    random_number = random.randint(1, 100)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer, rules
