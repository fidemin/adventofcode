import sys

from solution import solve

# from solution2 import solve as solve2

if __name__ == '__main__':
    args = sys.argv
    problem = sys.argv[1]
    filename = args[2]

    if problem == 'p1':
        print('answer:', solve(filename))
    # elif problem == 'p2':
    #     print('answer:', solve(filename, with_joker=True))
    else:
        raise RuntimeError(f'{problem} is not proper first argument. use p1 or p2')
