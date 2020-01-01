def flow(make_round):
    import prompt
    print('Welcome to the Brain Games!')
    current_question = make_round()
    print(current_question[2])
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    i = 0
    while i <= 3:
        if i == 3:
            print('Congratulations, {}!'.format(name))
            break
        print('Question:', current_question[0])
        player_answer = prompt.string('Your answer: ')
        player_answer = player_answer.lower()
        if player_answer == current_question[1]:
            i = i + 1
            print('Correct!')
            current_question = make_round()
        else:
            print1 = "'{}', is wrong answer ;(.".format(player_answer)
            print2 = "Correct answer was '{}'.".format(current_question[1])
            print(print1, print2)
            print("Let's try again, {}, !".format(name))
            break
