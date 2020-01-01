#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from brain_games.games.gcd import make_round
from brain_games.flow import flow


def main():
    flow(make_round)


if __name__ == '__main__':
    main()
