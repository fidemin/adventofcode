import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    day = args[0]
    part = args[1]
    sample = args[2] == "sample" if len(args) > 2 else False

    solve_module = __import__(f"aoc2025.{day}.solve", fromlist=["solve"])

    result = solve_module.solve(part, sample=sample)
    print(result)
