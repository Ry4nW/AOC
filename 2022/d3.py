f1 = open('./input/d3.txt', 'r')
lines = f1.readlines()

def p1(lines):
    total = 0
    for line in lines:
        print(len(line) // 2)
        p1 = line[:len(line) // 2]
        p2 = line[len(line) // 2:]
        
        for item in p1:
            if item in p2:
                if item.islower(): total += ord(item) - 96
                else: total += ord(item) - 38
                break
            
    return total

         
def p2(lines):
    total = 0
    for i in range(0, len(lines), 3):
        cur = [lines[i], lines[i+1], lines[i+2]]
        for char in cur[0]:
            if char in cur[1] and char in cur[2]:
                if char.islower(): total += ord(char) - 96
                else: total += ord(char) - 38
                break
            
    return total

print(f'Part 1: {p1(lines)}')
print(f'Part 2: {p2(lines)}')
