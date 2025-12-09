import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from itertools import product


def sqr_distance(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def find_closest(coordinates, target):
    key = lambda x: (x[0] - target[0]) ** 2 + (x[1] - target[1]) ** 2 + (x[2] - target[2]) ** 2
    return min(coordinates, key=key)


def closest_pairs(coordinates):
    pairs = product(coordinates, repeat=2)
    pairs = {tuple(sorted(pair)) for pair in pairs if pair[0] != pair[1]}
    return sorted(pairs, key=lambda x: sqr_distance(x[0], x[1]))

def first_part():
    circuits = []
    links = 0
    pairs = closest_pairs(coords)
    for pair in pairs[:limit]:
        for circuit in circuits:
            if pair[0] in circuit and pair[1] in circuit:
                break
            elif pair[0] in circuit:
                circuit.add(pair[1])
                links += 1
                ax.plot3D(*zip(*pair), color='green')
                break
            elif pair[1] in circuit:
                circuit.add(pair[0])
                links += 1
                ax.plot3D(*zip(*pair), color='green')
                break
        else:
            circuits.append({pair[0], pair[1]})
            links += 1
            ax.plot3D(*zip(*pair), color='red')

    # print(circuits)
    # print(*circuits, sep='\n')
    # circuits = {tuple(sorted(circuit)) for circuit in circuits}
    # comb_flag = True
    # while comb_flag:
    #     comb_flag = False
    #     circ_prod = set(map(lambda x: tuple(sorted(x)), product(circuits, repeat=2)))
    #     print(len(circuits), len(circ_prod))
    #     for circ1, circ2 in circ_prod:
    #         s1 = set(circ1)
    #         s2 = set(circ2)
    #         if s1 != s2:
    #             if s1 & s2:
    #                 combined = tuple(sorted(s1 | s2))
    #                 circuits.add(combined)
    #                 comb_flag = True
    #                 circuits.discard(circ1)
    #                 circuits.discard(circ2)
    # break
    from itertools import combinations

    circuits = combine_circuits(circuits)

    for circ in sorted(circuits, key=len, reverse=True)[:10]:
        print(len(circ), circ)


def combine_circuits(circuits):
    circuits = {tuple(sorted(circuit)) for circuit in circuits}

    while True:
        # Преобразуем в список множеств для работы
        circuits_list = [set(circuit) for circuit in circuits]
        merged = set()
        new_circuits = set()

        for i in range(len(circuits_list)):
            if i in merged:
                continue

            current = set(circuits_list[i])
            for j in range(i + 1, len(circuits_list)):
                if j in merged:
                    continue

                if current & circuits_list[j]:
                    current |= circuits_list[j]
                    merged.add(j)

            new_circuits.add(tuple(sorted(current)))

        # Если ничего не изменилось - выходим
        if new_circuits == circuits:
            break

        circuits = new_circuits

    print(f"Итоговое количество кластеров: {len(circuits)}")
    return [set(circuit) for circuit in circuits]


def second_part():
    circuits = []
    last_link = tuple()
    pairs = closest_pairs(coords)
    for pair in pairs:
        circuits = combine_circuits(circuits)
        if circuits and len(circuits[0]) == len(coords):
            break
        for circuit in circuits:
            if pair[0] in circuit and pair[1] in circuit:
                break
            elif pair[0] in circuit:
                circuit.add(pair[1])
                last_link = pair
                ax.plot3D(*zip(*pair), color='green')
                break
            elif pair[1] in circuit:
                circuit.add(pair[0])
                last_link = pair
                ax.plot3D(*zip(*pair), color='green')
                break
        else:
            circuits.append({pair[0], pair[1]})
            ax.plot3D(*zip(*pair), color='green')
    print(last_link)
    plt.show()


filename = "day_8.txt"
limit = 1000

# filename = "day_8_test.txt"
# limit = 10

ax = plt.axes(projection='3d')

with open(filename) as f:
    coords = tuple(tuple(map(int, line.split(','))) for line in f)

# first_part()
second_part()
