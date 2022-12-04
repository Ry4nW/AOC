f1 = open('./input/d4.txt', 'r')
lines = f1.readlines()

def p1(lines):
    total = 0
    for line in lines:
        cur = line.split(',')
        e1_range = cur[0].split('-')
        e2_range = cur[1].split('-')
        e1 = []; e2 = []
        
        for i in range(int(e1_range[0]), int(e1_range[1]) + 1):
            e1.append(str(i))
        for i in range(int(e2_range[0]), int(e2_range[1]) + 1):
            e2.append(str(i))  

        same = same2 = True
        for item in e1:
            if item not in e2:
                same = False
                break
        for item in e2:
            if item not in e1:
                same2 = False
                break

        if same or same2: total += 1
        
    return total

def p2(lines):
    total = 0
    for line in lines:
        cur = line.split(',')
        e1_range = cur[0].split('-')
        e2_range = cur[1].split('-')
        e1 = []; e2 = []
        
        for i in range(int(e1_range[0]), int(e1_range[1]) + 1):
            e1.append(str(i))
        for i in range(int(e2_range[0]), int(e2_range[1]) + 1):
            e2.append(str(i))  

        for item in e1:
            if item in e2:
                total += 1
                break
        
    return total

print(f'Part 1: {p1(lines)}')
print(f'Part 2: {p2(lines)}')

