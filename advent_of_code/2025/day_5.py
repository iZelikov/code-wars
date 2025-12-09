

def is_fresh(ing_id, ranges):
    for r in ranges:
        if ing_id >= r[0] and ing_id <= r[1]:
            return True
    return False


def combine_ranges(ranges_to_combine):
    comb_flag = True
    while comb_flag:
        combined = []
        comb_flag = False
        i = 0
        while i < len(ranges_to_combine) - 1:
            r1 = ranges_to_combine[i]
            r2 = ranges_to_combine[i + 1]
            if r1[1] >= r2[0]:
                if r1[1] <= r2[1]:
                    combined.append((r1[0], r2[1]))
                else:
                    combined.append((r1[0], r1[1]))
                i += 2
                comb_flag = True
            else:
                combined.append(ranges_to_combine[i])
                i += 1
        if i == len(ranges_to_combine) - 1:
            combined.append(ranges_to_combine[i])
        ranges_to_combine = combined
    return ranges_to_combine


with open("day_5.txt") as f:
    ranges, ids = f.read().split("\n\n")
    ranges = list(map(lambda x: (int(x.split("-")[0]), int(x.split("-")[1])), ranges.split("\n")))
    ranges.sort()
    ids = list(map(int, ids.strip().split("\n")))
    ids.sort()
    print(*ranges, sep="\n")
    print(*ids, sep="\n")
    total = 0
    for i in ids:
        if is_fresh(i, ranges):
            total += 1

    print(total)
    combined_ranges = combine_ranges(ranges)
    all_fresh_ids = 0
    for r in combined_ranges:
        all_fresh_ids += r[1] - r[0] + 1
    print(all_fresh_ids)