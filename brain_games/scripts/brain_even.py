#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from brain_games.game1 import check_even


def start():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')


def main():
    start()
    check_even()


if __name__ == '__main__':
    main()
