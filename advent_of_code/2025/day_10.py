"""
--- Day 10: Factory ---

Just across the hall, you find a large factory. Fortunately, the Elves here have plenty of time to decorate. Unfortunately, it's because the factory machines are all offline, and none of the Elves can figure out the initialization procedure.

The Elves do have the manual for the machines, but the section detailing the initialization procedure was eaten by a Shiba Inu. All that remains of the manual are some indicator light diagrams, button wiring schematics, and joltage requirements for each machine.

For example:

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}

The manual describes one machine per line. Each line contains a single indicator light diagram in [square brackets], one or more button wiring schematics in (parentheses), and joltage requirements in {curly braces}.

To start a machine, its indicator lights must match those shown in the diagram, where . means off and # means on. The machine has the number of indicator lights shown, but its indicator lights are all initially off.

So, an indicator light diagram like [.##.] means that the machine has four indicator lights which are initially off and that the goal is to simultaneously configure the first light to be off, the second light to be on, the third to be on, and the fourth to be off.

You can toggle the state of indicator lights by pushing any of the listed buttons. Each button lists which indicator lights it toggles, where 0 means the first light, 1 means the second light, and so on. When you push a button, each listed indicator light either turns on (if it was off) or turns off (if it was on). You have to push each button an integer number of times; there's no such thing as "0.5 presses" (nor can you push a button a negative number of times).

So, a button wiring schematic like (0,3,4) means that each time you push that button, the first, fourth, and fifth indicator lights would all toggle between on and off. If the indicator lights were [#.....], pushing the button would change them to be [...##.] instead.

Because none of the machines are running, the joltage requirements are irrelevant and can be safely ignored.

You can push each button as many times as you like. However, to save on time, you will need to determine the fewest total presses required to correctly configure all indicator lights for all machines in your list.

There are a few ways to correctly configure the first machine:

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

    You could press the first three buttons once each, a total of 3 button presses.
    You could press (1,3) once, (2,3) once, and (0,1) twice, a total of 4 button presses.
    You could press all of the buttons except (1,3) once each, a total of 5 button presses.

However, the fewest button presses required is 2. One way to do this is by pressing the last two buttons ((0,2) and (0,1)) once each.

The second machine can be configured with as few as 3 button presses:

[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}

One way to achieve this is by pressing the last three buttons ((0,4), (0,1,2), and (1,2,3,4)) once each.

The third machine has a total of six indicator lights that need to be configured correctly:

[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}

The fewest presses required to correctly configure it is 2; one way to do this is by pressing buttons (0,3,4) and (0,1,2,4,5) once each.

So, the fewest button presses required to correctly configure the indicator lights on all of the machines is 2 + 3 + 2 = 7.

Analyze each machine's indicator light diagram and button wiring schematics. What is the fewest button presses required to correctly configure the indicator lights on all of the machines?

Your puzzle answer was 542.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

All of the machines are starting to come online! Now, it's time to worry about the joltage requirements.

Each machine needs to be configured to exactly the specified joltage levels to function properly. Below the buttons on each machine is a big lever that you can use to switch the buttons from configuring the indicator lights to increasing the joltage levels. (Ignore the indicator light diagrams.)

The machines each have a set of numeric counters tracking its joltage levels, one counter per joltage requirement. The counters are all initially set to zero.

So, joltage requirements like {3,5,4,7} mean that the machine has four counters which are initially 0 and that the goal is to simultaneously configure the first counter to be 3, the second counter to be 5, the third to be 4, and the fourth to be 7.

The button wiring schematics are still relevant: in this new joltage configuration mode, each button now indicates which counters it affects, where 0 means the first counter, 1 means the second counter, and so on. When you push a button, each listed counter is increased by 1.

So, a button wiring schematic like (1,3) means that each time you push that button, the second and fourth counters would each increase by 1. If the current joltage levels were {0,1,2,3}, pushing the button would change them to be {0,2,2,4}.

You can push each button as many times as you like. However, your finger is getting sore from all the button pushing, and so you will need to determine the fewest total presses required to correctly configure each machine's joltage level counters to match the specified joltage requirements.

Consider again the example from before:

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}

Configuring the first machine's counters requires a minimum of 10 button presses. One way to do this is by pressing (3) once, (1,3) three times, (2,3) three times, (0,2) once, and (0,1) twice.

Configuring the second machine's counters requires a minimum of 12 button presses. One way to do this is by pressing (0,2,3,4) twice, (2,3) five times, and (0,1,2) five times.

Configuring the third machine's counters requires a minimum of 11 button presses. One way to do this is by pressing (0,1,2,3,4) five times, (0,1,2,4,5) five times, and (1,2) once.

So, the fewest button presses required to correctly configure the joltage level counters on all of the machines is 10 + 12 + 11 = 33.

Analyze each machine's joltage requirements and button wiring schematics. What is the fewest button presses required to correctly configure the joltage level counters on all of the machines?

"""

import re
from random import randint, sample
from time import time


class Machine:
    def __init__(self, config: str):
        self.target = list(re.findall(r"\[(.+)\]", config)[0])
        self.buttons = [tuple(map(int, x.split(','))) for x in re.findall(r"\(([^)]+)\)", config)]
        self.joltage_requirements = list(map(int, re.findall(r"\{(.+)\}", config)[0].split(',')))
        self.reset()

    def __str__(self):
        return f"{self.indicators} {self.joltage}"

    def __repr__(self):
        return f"Machine({self.target}, {self.indicators}, {self.buttons}, {self.joltage_requirements}, {self.joltage})"

    def switch_indicator(self, idx: int):
        states = {'.': '#', '#': '.'}
        self.indicators[idx] = states[self.indicators[idx]]

    def press_button(self, idx: int):
        for i in self.buttons[idx]:
            self.switch_indicator(i)

    def increase_joltage(self, idx: int):
        self.joltage[idx] += 1

    def press_joltage(self, idx: int):
        for i in self.buttons[idx]:
            self.increase_joltage(i)

    def reset(self):
        self.indicators = ['.'] * len(self.target)
        self.joltage = [0] * len(self.joltage_requirements)


def get_all_switches(machine: Machine) -> list:
    switches = []
    for i in range(2 ** len(machine.buttons)):
        switches.append(list(map(int, f"{i:0{len(machine.buttons)}b}")))
    return switches


def find_solution(machine) -> list:
    switches = get_all_switches(machine)
    good_switches = []
    for switch in switches:
        for i, flag in enumerate(switch):
            if flag:
                machine.press_button(i)
        # print(machine, switch)
        if machine.indicators == machine.target:
            good_switches.append(switch)
        machine.reset()
    good_switches.sort(key=lambda x: sum(x))
    return good_switches[0]


def fitness(machine: Machine, switches: list) -> tuple:
    for i, quantity in enumerate(switches):
        for _ in range(quantity):
            machine.press_joltage(i)
    rating = 0
    for i, joltage in enumerate(machine.joltage):
        rating += abs(joltage - machine.joltage_requirements[i])
    # print(machine.joltage, machine.joltage_requirements, (rating,sum(machine.joltage)))
    result = rating, sum(switches)
    machine.reset()
    return result


def create_population(machine: Machine, population_size: int) -> list:
    min_start_value = 0
    max_start_value = 5
    return [[randint(min_start_value, max_start_value) for _ in range(len(machine.buttons))] for _ in
            range(population_size)]


def mutate(switches, mutation_rate) -> list:
    switches = switches.copy()
    for i in range(len(switches)):
        if randint(0, 100) < mutation_rate * 100:
            switches[i] += randint(-1, 1)
            if switches[i] < 0:
                switches[i] = 0
    return switches


def tournament(population, machine):
    winners = []
    for _ in range(len(population) // 2):
        p1, p2 = sample(population, 2)
        if fitness(machine, p1) < fitness(machine, p2):
            winners.append(p1.copy())
        else:
            winners.append(p2.copy())
    return winners

def crossover(p1, p2):
    cross = randint(0, len(p1) - 1)
    return p1[:cross] + p2[cross:]


def get_evolution_solution(machine: Machine) -> list:
    population_size = 1000
    mutation_rate = 0.1
    generations = 1000
    population = create_population(machine, population_size)
    for i in range(generations):
        population = tournament(population, machine)
        l = len(population)
        for j in range(l):
            # child = crossover(population[j], population[randint(0, l - 1)])
            # population.append(mutate(child, mutation_rate))
            population.append(mutate(population[j], mutation_rate))
    return min(population, key=lambda x: fitness(machine, x))


def fist_part():
    with open(filename) as f:
        lines = f.read().splitlines()
        machines = [Machine(line) for line in lines]
        total = 0
        for machine in machines:
            total += sum(find_solution(machine))

        print(total)

def find_optimal(machine: Machine, buttons: list):
    if sum(buttons) >= optimal_presses[0]:
        return
    machine.reset()
    for i, count in enumerate(buttons):
        for _ in range(count):
            machine.press_joltage(i)

    if machine.joltage == machine.joltage_requirements:
        optimal_presses[0] = sum(buttons)
        optimal_presses[1] = buttons.copy()
        # print(optimal_presses)
    elif sum(buttons) < optimal_presses[0]:
        for i, joltage in enumerate(machine.joltage):
            if joltage > machine.joltage_requirements[i]:
                break
        else:
            for i, button in enumerate(buttons):
                new_buttons = buttons[:i] + [button + 1] + buttons[i + 1:]
                find_optimal(machine, new_buttons)




def second_part():
    with open(filename) as f:
        lines = f.read().splitlines()
        machines = [Machine(line) for line in lines]
        total = 0
        for i, machine in enumerate(machines):
            start = time()
            result = get_evolution_solution(machine)
            total += sum(result)
            print(i, result, fitness(machine, result), sum(result), f'- {int(time() - start)}s')
        print(total)

def part_2():
    global optimal_presses
    with open(filename) as f:
        lines = f.read().splitlines()
        machines = [Machine(line) for line in lines]
        total = 0
        for i, machine in enumerate(machines):
            find_optimal(machine, [0]*len(machine.buttons))
            print(i, optimal_presses)
            total+=optimal_presses[0]
            optimal_presses = [float('inf'), []]
        print(total)


filename = "day_10.txt"
# filename = "day_10_test.txt"

# fist_part()
# second_part()

optimal_presses = [float('inf'), []]
part_2()