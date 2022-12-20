f1 = open('./input/d10.txt', 'r')
lines = f1.readlines()


def p1(lines):
    register = 1
    cycle = 1
    sig_strengths = 0
    
    for instruc in lines:
        instruc = instruc.strip()
        if (cycle - 20) % 40 == 0: 
            sig_strengths += cycle * register
        
        if instruc != "noop":
            add_x = instruc.split(' ')
            
            if (cycle + 19) % 40 == 0:
                sig_strengths += (cycle + 1) * register
            
            cycle += 2
            register += int(add_x[1])
        else:
            cycle += 1
    
    return sig_strengths
            
    
def p2(lines):
    register = 1
    cycle = 1
    crt = []
    
    for instruc in lines:
        instruc = instruc.strip()

        if instruc != "noop":
            add_x = instruc.split(' ')
            if cycle - 1 in (register - 1, register, register + 1):
                crt.append('#')
            else:
                crt.append('.')   
            if cycle % 40 == 0: crt.append('\n'); register += 40
        
            cycle += 1
            
            if cycle - 1 in (register - 1, register, register + 1):
                crt.append('#')
            else:
                crt.append('.')  
            if cycle % 40 == 0: crt.append('\n'); register += 40
            
            cycle += 1  
            register += int(add_x[1])

        else:
            if cycle - 1 in (register - 1, register, register + 1):
                crt.append('#')
            else:
                crt.append('.')
            if cycle % 40 == 0: crt.append('\n'); register += 40
            cycle += 1
            
    return ''.join(crt)

# print(f'Part 1: {p1(lines)}')
print(p2(lines))
