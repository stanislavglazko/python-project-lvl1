#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from brain_games.games.game1_even import check_even
from brain_games.games.flow import flow


def start():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')


def main():
    start()
    flow((check_even(), check_even(), check_even()))


if __name__ == '__main__':
    main()
