def find_path(connections, start, end, visited=None):
    global total
    if visited is None:
        visited = {start}
    if start == end:
        return [start]
    elif start not in connections:
        return []
    else:
        all_paths = []
        for nxt in connections[start]:
            new_visited = visited.copy()
            if nxt in new_visited:
                continue
            else:
                new_visited.add(nxt)
            paths = find_path(connections, nxt, end, new_visited)
            for path in paths:
                if path:
                    if isinstance(path, list):
                        all_paths.append([start] + path)
                    else:
                        all_paths.append([start, path])
                else:
                    all_paths.append([start])
        return all_paths

def find_path_count_with_memo(graph, start, end):
    if start == end:
        return 1
    elif start not in graph:
        return 0
    elif start in find_path_count_with_memo.memo:
        return find_path_count_with_memo.memo[start]
    else:
        total = 0
        for node in graph[start]:
            path_count = find_path_count_with_memo(graph, node, end)
            total += path_count
        find_path_count_with_memo.memo[start] = total
        return total



def part_1():
    paths = find_path(connections, "you", "out")
    print(len(paths))


def part_2():
    find_path_count_with_memo.memo = {}
    svr_to_fft = find_path_count_with_memo(connections, "svr", "fft")
    find_path_count_with_memo.memo = {}
    fft_to_dac = find_path_count_with_memo(connections, "fft", "dac")
    find_path_count_with_memo.memo = {}
    dac_to_out = find_path_count_with_memo(connections, "dac", "out")
    # print(svr_to_fft, fft_to_dac, dac_to_out)
    print(svr_to_fft * fft_to_dac * dac_to_out)

filename = "day_11"
# filename = "day_11_test"

with open(filename) as f:
    lines = f.read().splitlines()
    connections = {}
    for line in lines:
        connection = line.split()
        connections[connection[0][:-1]] = connection[1:]
    # print(connections)

part_1()
part_2()
