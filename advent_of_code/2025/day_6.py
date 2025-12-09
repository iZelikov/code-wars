from functools import reduce
from itertools import zip_longest

def get_numbers(p):
    return map(int, p)

def get_numbers2(p):
    n = list(map(lambda x: x[::-1], p))
    return map(lambda x: int("".join(x)), zip_longest(*n, fillvalue=" "))

def first_part():
    with open("day_6.txt") as f:
        actions = {"+": lambda x, y: x + y, "*": lambda x, y: x * y, "-": lambda x, y: x - y, "/": lambda x, y: x / y,
                   "^": lambda x, y: x ** y, "=": lambda x, y: f"{x}={y}"}
        problems = f.read().splitlines()
        problems = zip(*map(lambda x: x.split(), problems))
        total = 0
        for problem in problems:
            numbers = get_numbers(problem[:-1])
            op = actions[problem[-1]]
            answer = reduce(op, numbers)
            total += answer

        print(total)

def second_part():
    with open("day_6.txt") as f:
        actions = {"+": lambda x, y: x + y, "*": lambda x, y: x * y, "-": lambda x, y: x - y, "/": lambda x, y: x / y,
                   "^": lambda x, y: x ** y, "=": lambda x, y: f"{x}={y}"}
        problems = f.read().splitlines()
        problems = zip_longest(*problems, fillvalue=" ")
        numbers = []
        total = 0
        answer = 0
        op = actions["+"]
        for problem in problems:
            if problem[-1] in actions:
                if numbers:
                    answer = reduce(op, numbers)
                total+=answer
                op = actions[problem[-1]]
                numbers = []
                n = int("".join(problem[:-1]))
                numbers.append(n)
            else:
                ns = "".join(problem[:-1]).strip()
                if ns.isdigit():
                    n = int(ns)
                    numbers.append(n)
        ns = "".join(problem[:-1]).strip()
        answer = reduce(op, numbers)
        total += answer

        print(total)

first_part()
second_part()
