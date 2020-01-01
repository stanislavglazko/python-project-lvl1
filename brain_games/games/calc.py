def make_round():
    import random
    rules = 'What is the result of the expression?'
    random1 = random.randint(1, 100)
    random3 = random.randint(1, 100)
    random2 = random.randint(1, 3)
    if random2 == 1:
        correct_answer = str(random1 + random3)
        random2 = "+"
    elif random2 == 2:
        correct_answer = str(random1 - random3)
        random2 = "-"
    else:
        correct_answer = str(random1 * random3)
        random2 = "*"
    random_number = str(random1) + " " + str(random2) + " " + str(random3)
    return random_number, correct_answer, rules
