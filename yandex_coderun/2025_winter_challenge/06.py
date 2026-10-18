"""
6. Ориентирование на местности

Последние приготовления. Кодерун отрабатывает навык ориентирования в двумерной Долине Синтаксиса. Он начинает движение из точки ( 0 , 0 ) (0,0) и выполняет серию команд, проверяя, как меняются расстояния до установленных сигнальных меток.

Возможные команды:

N — движение на север: ( x , y ) (x,y) → → ( x , y + 1 ) (x,y+1)

S — движение на юг: ( x , y ) (x,y) → → ( x , y − 1 ) (x,y−1)

W — движение на запад: ( x , y ) (x,y) → → ( x − 1 , y ) (x−1,y)

E — движение на восток: ( x , y ) (x,y) → → ( x + 1 , y ) (x+1,y)

После каждой команды вычисляется сумма манхэттенских расстояний от текущего положения Кодеруна до всех N N меток.

Манхэттенское расстояние между двумя точками определяется как сумма модулей разностей их координат. Для точек ( x 1 x1​, y 1 y1​) и ( x 2 x2​, y 2 y2​) манхэттенское расстояние равно: ∣ x 1 − x 2 ∣ + ∣ y 1 − y 2 ∣ ∣x1​−x2​∣+∣y1​−y2​∣.

Нужно вывести общую сумму расстояний от Кодеруна до всех меток после каждой команды.
Формат ввода

В первой строке даны два целых числа N N ( 1 ≤ N ≤ 100   000 1≤N≤100000) и  M M ( 1 ≤ M ≤ 300   000 1≤M≤300000) — количество меток и количество команд.

В следующих N N строках заданы координаты меток: по два целых числа x x и  y y ( ∣ x ∣ , ∣ y ∣ ≤ 1   000   000 ∣x∣,∣y∣≤1000000) в каждой строке.

В последней строке вводится строка из  M M символов, задающая команды для движения.
Формат вывода

Выведите суммарное расстояние до всех меток после выполнения каждой инструкции.
"""


def distance(x, y, points):
    result = 0
    for point in points:
        result += abs(x - point[0]) + abs(y - point[1])
    return result

def difference(x, y, move, distance_0):
    if move in "NS":
        if (None, y, move) in memo:
            return memo[(None, y, move)]
        x1 = x + moves[move][0]
        y1 = y + moves[move][1]
        d = distance(x1, y1, points) - distance_0
        memo[(None, y, move)] = d
        return d
    elif move in "WE":
        if (x, None, move) in memo:
            return memo[(x, None, move)]
        x1 = x + moves[move][0]
        y1 = y + moves[move][1]
        d = distance(x1, y1, points) - distance_0
        memo[(x, None, move)] = d
        return d

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
commands = input()
moves = {"N": (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)}
x = y = 0
sum_distance = distance(x, y, points)
memo = {}
for move in commands:
    diff = difference(x, y, move, sum_distance)
    x += moves[move][0]
    y += moves[move][1]
    sum_distance += diff
    print(sum_distance)
