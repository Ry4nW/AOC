data = [x.rstrip() for x in open("input.txt").readlines()]

print(sum([int(x) * list(map(sorted, zip(*map(str.split, data))))[1].count(x) for x in list(map(sorted, zip(*map(str.split, data))))[0]]))
