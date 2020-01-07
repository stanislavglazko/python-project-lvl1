import prompt


def flow(game):
    print('Welcome to the Brain Games!')
    print(game.rules())
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    i = 0
    while i < 3:
        round = game.make_round()
        current_question = round[0]
        good_answer = str(round[1])
        print('Question:', current_question)
        player_answer = prompt.string('Your answer: ')
        player_answer = player_answer.lower()
        if not player_answer == good_answer:
            print1 = "'{}', is wrong answer ;(.".format(player_answer)
            print2 = "Correct answer was '{}'.".format(good_answer)
            print(print1, print2)
            print("Let's try again, {}, !".format(name))
            break
        i = i + 1
        print('Correct!')
    else:
        print('Congratulations, {}!'.format(name))
