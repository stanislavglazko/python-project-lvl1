def calc():
    import random
    a = []
    b = []
    c = [0, 0]
    for i in range(1, 4):
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
        a.append(random_number)
        b.append(correct_answer)
    c[0] = a
    c[1] = b
    return c
