def check_even():
    import prompt
    import random
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    i = 0
    while i <= 3:
        if i == 3:
            print('Congratulations, {}!'.format(name))
            break
        random_number = random.randint(1, 100)
        check = random_number % 2
        if check == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('Question:', random_number)
        player_answer = prompt.string('Your answer: ')
        player_answer = player_answer.lower()
        if player_answer == correct_answer:
            i = i + 1
            print('Correct!')
        else:
            pa = "'{}', is wrong answer ;(.".format(player_answer)
            ca = "Correct answer was '{}'.".format(correct_answer)
            print(pa, ca)
            print("Let's try again, {}, !".format(name))
            break
