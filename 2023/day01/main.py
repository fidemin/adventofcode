import sys

from solution import solution1

if __name__ == '__main__':
    args = sys.argv
    filename = args[1]

    print('answer:', solution1(filename))
