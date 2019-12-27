def check_even():
    import random
    a = []
    b = []
    c = [0, 0]
    for i in range(1, 4):
        random_number = random.randint(1, 100)
        check = random_number % 2
        if check == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        a.append(random_number)
        b.append(correct_answer)
    c[0] = a
    c[1] = b
    return c
