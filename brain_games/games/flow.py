def flow(x):
    import prompt
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    i = 0
    while i <= 3:
        if i == 3:
            print('Congratulations, {}!'.format(name))
            break
        print('Question:', x[0][i])
        player_answer = prompt.string('Your answer: ')
        player_answer = player_answer.lower()
        if player_answer == x[1][i]:
            i = i + 1
            print('Correct!')
        else:
            print1 = "'{}', is wrong answer ;(.".format(player_answer)
            print2 = "Correct answer was '{}'.".format(x[1][i])
            print(print1, print2)
            print("Let's try again, {}, !".format(name))
            break
