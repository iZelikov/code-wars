import re

filename = "day_12"
# filename = "day_12_test"

with open(filename) as f:
    lines = f.read().splitlines()

shape_transform = {"#": 1, ".": 0}
shapes = []
containers = []
for i in range(5):
    shape = [list(map(lambda x: shape_transform[x], line)) for line in lines[i * 5 + 1:i * 5 + 4]]
    shapes.append(shape)

for line in lines[30:]:
    region = tuple(int(x) for x in re.findall(r"(\d+)x(\d+):", line)[0])
    presents = tuple(map(int, re.findall(r" (\d+)", line)))
    containers.append((region, presents))
