f1 = open('./input/d2.txt', 'r')
lines = f1.readlines()

wins = {'Z':'B', 'Y':'A', 'X':'C'}
wins1 = {'B':'Z', 'A':'Y', 'C':'X'}
draws = {'A':'X', 'B':'Y', 'C':'Z'}
vals = {'X':1, 'Y':2, 'Z':3}


def p1(lines):
    total = 0
    for line in lines:
        cur = line.split(' ')
        elf = cur[0]
        play = cur[1].strip()
        
        if play == 'Y': total += 2
        elif play == 'X': total += 1
        else: total += 3
        
        if wins[play] == elf: total += 6
        elif draws[elf] == play: total += 3

    print(total)
 
    
def p2(lines):
    total = 0
    for line in lines:
        cur = line.split(' ')
        elf = cur[0]
        play = cur[1].strip()
        
        if play == 'Y':
            total += vals[draws[elf]] + 3
        elif play == 'X':
            win = wins1[elf]
            draw = draws[elf]
            for val in vals:
                if val != win and val != draw:
                    total += vals[val]
                    break
        else:
            total += vals[wins1[elf]] + 6
    return total

print(f'Part 1: {p1(lines)}')
print(f'Part 2: {p2(lines)}')
