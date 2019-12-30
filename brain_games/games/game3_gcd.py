def nod():
    import random
    random1 = random.randint(1, 100)
    random2 = random.randint(1, 100)
    random_number = str(random1) + " " + str(random2)
    while random1 != 0 and random2 != 0:
        if random1 > random2:
            random1 %= random2
        else:
            random2 %= random1
    correct_answer = str(random1 + random2)
    return random_number, correct_answer
