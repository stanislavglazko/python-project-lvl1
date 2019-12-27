from brain_games.games.flow import flow
from brain_games.games.game2_calc import calc 


def start():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')


def main():
    start()
    flow(calc())


if __name__ == '__main__':
    main()
