def make_round():
    import random
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    random_number = random.randint(1, 100)
    delitel = 2
    while random_number % delitel != 0:
        delitel += 1
    if delitel == random_number:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer, rules
