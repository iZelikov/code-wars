"""
5. Маршрут до Пика Кода

Кодерун планирует маршрут на Пик Кода. На трёхмерной карте расставлены N N контрольных точек, через которые может пролегать путь, каждая из которых имеет координаты x i xi​, y i yi​ и  z i zi​.

Количество усилий, необходимых для прохождения перехода между двумя точками i i и  j j, равно минимальному из модулей разностей их координат по осям x x, y y и  z z — c o s t [ i ] [ j ] = m i n ( ∣ x i − x j ∣ , ∣ y i − y j ∣ , ∣ z i − z j ∣ ) cost[i][j]=min(∣xi​−xj​∣,∣yi​−yj​∣,∣zi​−zj​∣).

Нужно соединить все контрольные точки ровно N − 1 N−1 переходами так, чтобы от любой можно было добраться до любой другой (возможно, через промежуточные точки), и общее количество усилий было минимальным.
Формат ввода

В первой строке вводится число N N ( 1 ≤ N ≤ 100000 1≤N≤100000) — количество контрольных точек.

В следующих N N строках вводятся по три числа x i xi​, y i yi​, z i zi​ ( − 1 09 ≤ x i , y i , z i ≤ 1 09 −109≤xi​,yi​,zi​≤109) — координаты очередной контрольной точки.
Формат вывода

Выведите минимальное суммарное количество усилий, необходимых для соединения всех контрольных точек N − 1 N−1 переходами.
Примечание

В первом примере минимальная разница по  y y координате, она равна ∣ 6 − 9 ∣ = 3 ∣6−9∣=3. Достаточно проложить один переход для соединения двух контрольных точек.

Во втором примере разницы по всем координатам равны. Можно проложить переход от первой контрольной точки до второй и от второй до третьей, в итоге все точки окажутся связанными.

"""
from itertools import permutations, pairwise, combinations


def distance(a, b):
    return min(abs(a[i] - b[i]) for i in range(3))


def way(points):
    return sum(distance(p1, p2) for p1, p2 in pairwise(points))


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

pairs = combinations(points, 2)
pairs = sorted(pairs, key = way)

# all_ways = {}
# for pair in pairs:
#     all_ways.setdefault(pair[0], []).append((pair[1], way(pair)))
#     all_ways.setdefault(pair[1], []).append((pair[0], way(pair)))
#
# print(all_ways)


sequence = [pairs[0][0], pairs[0][1]]

while len(sequence) < n:
    for pair in pairs:
        if pair[0] not in sequence:
            if pair[1] == sequence[0]:
                sequence.insert(0, pair[0])
                break
            elif pair[1] == sequence[-1]:
                sequence.append(pair[0])
                break
        if pair[1] not in sequence:
            if pair[0] == sequence[0]:
                sequence.insert(0, pair[1])
                break
            elif pair[0] == sequence[-1]:
                sequence.append(pair[1])
                break

print(way(sequence))
