"""
--- Day 6: Trash Compactor ---

After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!

A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.

As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her math homework.

Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to be either added (+) or multiplied (*) together.

However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:

123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +

Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.

So, this worksheet contains four problems:

    123 * 45 * 6 = 33210
    328 + 64 + 98 = 490
    51 * 387 * 215 = 4243455
    64 + 23 + 314 = 401

To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.

Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.

Solve the problems on the math worksheet. What is the grand total found by adding together all of the answers to the individual problems?

Your puzzle answer was 4583860641327.
--- Part Two ---

The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +

Reading the problems right-to-left one column at a time, the problems are now quite different:

    The rightmost problem is 4 + 431 + 623 = 1058
    The second problem from the right is 175 * 581 * 32 = 3253600
    The third problem from the right is 8 + 248 + 369 = 625
    Finally, the leftmost problem is 356 * 24 * 1 = 8544

Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?

"""

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
