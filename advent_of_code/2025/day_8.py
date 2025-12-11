"""
--- Day 8: Playground ---

Equipped with a new understanding of teleporter maintenance, you confidently step onto the repaired teleporter pad.

You rematerialize on an unfamiliar teleporter pad and find yourself in a vast underground space which contains a giant playground!

Across the playground, a group of Elves are working on setting up an ambitious Christmas decoration project. Through careful rigging, they have suspended a large number of small electrical junction boxes.

Their plan is to connect the junction boxes with long strings of lights. Most of the junction boxes don't provide electricity; however, when two junction boxes are connected by a string of lights, electricity can pass between those two junction boxes.

The Elves are trying to figure out which junction boxes to connect so that electricity can reach every junction box. They even have a list of all of the junction boxes' positions in 3D space (your puzzle input).

For example:

162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689

This list describes the position of 20 junction boxes, one per line. Each position is given as X,Y,Z coordinates. So, the first junction box in the list is at X=162, Y=817, Z=812.

To save on string lights, the Elves would like to focus on connecting pairs of junction boxes that are as close together as possible according to straight-line distance. In this example, the two junction boxes which are closest together are 162,817,812 and 425,690,689.

By connecting these two junction boxes together, because electricity can flow between them, they become part of the same circuit. After connecting them, there is a single circuit which contains two junction boxes, and the remaining 18 junction boxes remain in their own individual circuits.

Now, the two junction boxes which are closest together but aren't already directly connected are 162,817,812 and 431,825,988. After connecting them, since 162,817,812 is already connected to another junction box, there is now a single circuit which contains three junction boxes and an additional 17 circuits which contain one junction box each.

The next two junction boxes to connect are 906,360,560 and 805,96,715. After connecting them, there is a circuit containing 3 junction boxes, a circuit containing 2 junction boxes, and 15 circuits which contain one junction box each.

The next two junction boxes are 431,825,988 and 425,690,689. Because these two junction boxes were already in the same circuit, nothing happens!

This process continues for a while, and the Elves are concerned that they don't have enough extension cables for all these circuits. They would like to know how big the circuits will be.

After making the ten shortest connections, there are 11 circuits: one circuit which contains 5 junction boxes, one circuit which contains 4 junction boxes, two circuits which contain 2 junction boxes each, and seven circuits which each contain a single junction box. Multiplying together the sizes of the three largest circuits (5, 4, and one of the circuits of size 2) produces 40.

Your list contains many junction boxes; connect together the 1000 pairs of junction boxes which are closest together. Afterward, what do you get if you multiply together the sizes of the three largest circuits?

Your puzzle answer was 112230.
--- Part Two ---

The Elves were right; they definitely don't have enough extension cables. You'll need to keep connecting junction boxes together until they're all in one large circuit.

Continuing the above example, the first connection which causes all of the junction boxes to form a single circuit is between the junction boxes at 216,146,977 and 117,168,530. The Elves need to know how far those junction boxes are from the wall so they can pick the right extension cable; multiplying the X coordinates of those two junction boxes (216 and 117) produces 25272.

Continue connecting the closest unconnected pairs of junction boxes together until they're all in the same circuit. What do you get if you multiply together the X coordinates of the last two junction boxes you need to connect?

"""

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
