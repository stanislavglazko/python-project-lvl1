from brain_games.games.flow import flow
from brain_games.games.game3_gcd import nod


def start():
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.')


def main():
    start()
    flow((nod(), nod(), nod()))


if __name__ == '__main__':
    main()
