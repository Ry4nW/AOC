f1 = open('./input/d1.txt', 'r')
inp = f1.read()

def p1(vals):
    max_cal = 0
    for elves in vals.split('\n\n'):
        cur = 0
        for food in elves.split():
            cur += int(food)
        max_cal = max(max_cal, cur)
    return max_cal

def p2(vals):
    top = [0, 0, 0]
    for elves in vals.split('\n\n'):
        cur = 0
        for food in elves.split():
            cur += int(food)
        if cur > top[0]:
            top[2] = top[1]; top[1] = top[0]
            top[0] = cur
        elif cur > top[1]:
            top[2] = top[1]
            top[1] = cur
        elif cur > top[2]:
            top[2] = cur
    return sum(top)


print(f'Part 1: {p1(inp)}')
print(f'Part 2: {p2(inp)}')
