#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from brain_games.games.game4_progression import progression
from brain_games.games.flow import flow


def start():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?')


def main():
    start()
    flow((progression(), progression(), progression()))


if __name__ == '__main__':
    main()
