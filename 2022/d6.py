f1 = open('./input/d6.txt', 'r')
lines = f1.read()


def p1(lines):
    for i in range(len(lines) - 4):
        cur = set(lines[i:i+4])
        if len(cur) == 4: return i + 4
    
    
def p2(lines):
    for i in range(len(lines) - 14):
        cur = set(lines[i:i+14])
        if len(cur) == 14: return i + 14  

print(f'Part 1: {p1(lines)}')
print(f'Part 2: {p2(lines)}')
