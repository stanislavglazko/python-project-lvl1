def progression():
    import random
    step = random.randint(1, 10)
    first_element = random.randint(1, 10)
    a_progression = []
    for i in range(1, 11):
        i_element = first_element + (i - 1) * step
        a_progression.append(i_element)
    secret_progression = a_progression
    secret_element = random.randint(0, 9)
    correct_answer = str(a_progression[secret_element])
    secret_progression[secret_element] = ".."
    random_number = secret_progression
    return random_number, correct_answer
