import random


def make_round():
    step = random.randint(1, 10)
    first_element = random.randint(1, 10)
    a_progression = []
    for i in range(1, 11):
        i_element = str(first_element + (i - 1) * step)
        a_progression.append(i_element)
    secret_element = random.randint(0, 9)
    correct_answer = a_progression[secret_element]
    a_progression[secret_element] = ".."
    question = ''
    for i in a_progression:
        question = question + i + ' '
    return question, correct_answer


def rules():
    return 'What number is missing in the progression?'


def main():
    make_round()
    rules()


if __name__ == '__main__':
    main()
