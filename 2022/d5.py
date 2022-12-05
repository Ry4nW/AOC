import copy

f1 = open('./input/d5.txt', 'r')
lines = f1.readlines()
instructs = lines[10:]
crates = { i : [] for i in range(1, 10) }

for i in range(1, 35, 4):
    for j in range(8):
        cur = lines[j][i]
        if cur != ' ': crates[int(lines[8][i])].append(cur)
        
crate1 = copy.deepcopy(crates)
crate2 = copy.deepcopy(crates)

def p1(crates, instructs):
    for instruct in instructs:
        cur = instruct.split(' ')
        fro = int(cur[3]); to = int(cur[5])
        
        for _ in range(int(cur[1])):
            crates[to].insert(0, crates[fro].pop(0))
    
    top = ''
    for stack in crates:
        top += crates[stack][0]
        
    return top
    
def p2(crates, instructs):
    for instruct in instructs:
        cur = instruct.split(' ')
        amt = int(cur[1])
        fro = int(cur[3]); to = int(cur[5])
        
        for i in range(amt - 1, -1, -1):
            crates[to].insert(0, crates[fro][i])
        del crates[fro][:amt]
            
    top = ''
    for stack in crates:
        top += crates[stack][0]
        
    return top

print(f'Part 1: {p1(crate1, instructs)}')
print(f'Part 2: {p2(crate2, instructs)}')
