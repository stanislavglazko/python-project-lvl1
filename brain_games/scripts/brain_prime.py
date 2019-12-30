#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from brain_games.games.game5_prime import prime
from brain_games.games.flow import flow


def start():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def main():
    start()
    flow((prime(), prime(), prime()))


if __name__ == '__main__':
    main()
