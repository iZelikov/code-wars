"""
--- Day 9: Movie Theater ---

You slide down the firepole in the corner of the playground and land in the North Pole base movie theater!

The movie theater has a big tile floor with an interesting pattern. Elves here are redecorating the theater by switching out some of the square tiles in the big grid they form. Some of the tiles are red; the Elves would like to find the largest rectangle that uses red tiles for two of its opposite corners. They even have a list of where the red tiles are located in the grid (your puzzle input).

For example:

7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3

Showing red tiles as # and other tiles as ., the above arrangement of red tiles would look like this:

..............
.......#...#..
..............
..#....#......
..............
..#......#....
..............
.........#.#..
..............

You can choose any two red tiles as the opposite corners of your rectangle; your goal is to find the largest rectangle possible.

For example, you could make a rectangle (shown as O) with an area of 24 between 2,5 and 9,7:

..............
.......#...#..
..............
..#....#......
..............
..OOOOOOOO....
..OOOOOOOO....
..OOOOOOOO.#..
..............

Or, you could make a rectangle with area 35 between 7,1 and 11,7:

..............
.......OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
.......OOOOO..
..............

You could even make a thin rectangle with an area of only 6 between 7,3 and 2,3:

..............
.......#...#..
..............
..OOOOOO......
..............
..#......#....
..............
.........#.#..
..............

Ultimately, the largest rectangle you can make in this example has area 50. One way to do this is between 2,5 and 11,1:

..............
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..............
.........#.#..
..............

Using two red tiles as opposite corners, what is the largest area of any rectangle you can make?

Your puzzle answer was 4777824480.
--- Part Two ---

The Elves just remembered: they can only switch out tiles that are red or green. So, your rectangle can only include red or green tiles.

In your list, every red tile is connected to the red tile before and after it by a straight line of green tiles. The list wraps, so the first red tile is also connected to the last red tile. Tiles that are adjacent in your list will always be on either the same row or the same column.

Using the same example as before, the tiles marked X would be green:

..............
.......#XXX#..
.......X...X..
..#XXXX#...X..
..X........X..
..#XXXXXX#.X..
.........X.X..
.........#X#..
..............

In addition, all of the tiles inside this loop of red and green tiles are also green. So, in this example, these are the green tiles:

..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............

The remaining tiles are never red nor green.

The rectangle you choose still must have red tiles in opposite corners, but any other tiles it includes must now be red or green. This significantly limits your options.

For example, you could make a rectangle out of red and green tiles with an area of 15 between 7,3 and 11,1:

..............
.......OOOOO..
.......OOOOO..
..#XXXXOOOOO..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............

Or, you could make a thin rectangle with an area of 3 between 9,7 and 9,5:

..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXXOXX..
.........OXX..
.........OX#..
..............

The largest rectangle you can make in this example using only red and green tiles has area 24. One way to do this is between 9,5 and 2,3:

..............
.......#XXX#..
.......XXXXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
.........XXX..
.........#X#..
..............

Using two red tiles as opposite corners, what is the largest area of any rectangle you can make using only red and green tiles?

"""


import itertools
import matplotlib.pyplot as plt

def get_square(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    return (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)


def create_matrix(coords: list[tuple[int, int]]):
    coords = set(coords)
    max_x = max(coords, key=lambda x: x[0])[0]
    max_y = max(coords, key=lambda x: x[1])[1]
    matrix = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if (x, y) in coords:
                matrix[y][x] = "#"
    return matrix


def fill_hotizontal(matrix: list[list[str]], char: str = "#"):
    start_green = False
    stop_green = False
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == char:
                start_green = not start_green
            elif start_green and matrix[y][x] == ".":
                matrix[y][x] = "G"


def transpose(matrix: list[list[str]]):
    return list([list(line) for line in zip(*matrix)])  # transpose matrix


def fill_green(matrix: list[list[str]]):
    fill_hotizontal(matrix)
    matrix = transpose(matrix)
    fill_hotizontal(matrix)
    matrix = transpose(matrix)
    return matrix


def print_matrix(matrix: list[list[str]]):
    print(*matrix, sep='\n')


def check_line(matrix: list[list[str]], start: tuple[int, int], end: tuple[int, int]):
    print(start, end)
    if start[0] == end[0]:
        s, e = sorted([start[1], end[1]])
        print(s, e)
        for y in range(s + 1, e):
            if matrix[y][start[0]] != "G":
                return False

    if start[1] == end[1]:
        s, e = sorted([start[0], end[0]])
        print(s, e)
        for x in range(s + 1, e):
            if matrix[start[1]][x] != "G":
                return False
    return True


def check_rectangle(matrix: list[list[str]], corner1: tuple[int, int], corner2: tuple[int, int]):
    corner3 = (corner2[0], corner1[1])
    corner4 = (corner1[0], corner2[1])
    corners = [corner1, corner2, corner3, corner4]
    for corner in corners:
        if matrix[corner[1]][corner[0]] == ".":
            return False
    lines = [
        (corner1, corner3),
        (corner1, corner4),
        (corner2, corner3),
        (corner2, corner4)
    ]
    good = 0
    for start_point, end_point in lines:
        if start_point != end_point:
            if check_line(matrix, start_point, end_point):
                good += 1
    if good < 3:
        return False
    return True


def first_part():
    squares = list(itertools.product(coords, repeat=2))
    squares.sort(key=lambda x: get_square(x[0], x[1]))
    # print(*squares, sep='\n')
    print(get_square(*squares[-1]))


# not work
# def second_part():
#     matrix = create_matrix(coords)
#     print_matrix(matrix)
#     matrix = fill_green(matrix)
#     print_matrix(matrix)
#     print(check_rectangle(matrix, (9, 5), (2,3)))
#     squares = list(itertools.product(coords, repeat=2))
#     squares.sort(key=lambda x: get_square(x[0], x[1]), reverse=True)
#     for square in squares:
#         if check_rectangle(matrix, *square):
#             print(get_square(*square), square)
#             break

def graph():
    plt.scatter(*zip(*coords))
    plt.show()

filename = "day_9.txt"
# filename = "day_9_test.txt"

with open(filename) as f:
    coords = tuple(tuple(map(int, line.split(','))) for line in f)

first_part()
print(get_square((94645,50248), (5942,67632)))

