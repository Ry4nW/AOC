f1 = open('./input/d8.txt', 'r')
lines = f1.readlines()


def p1(lines):
    matrix = [[el.strip() for el in row] for row in lines]
    for i in range(len(matrix) - 1): matrix[i].pop()
    total = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if i in (len(matrix) - 1, 0) or j in (len(matrix[0]) - 1, 0):
                total += 1
                continue
            
            cur = int(matrix[i][j])
            
            select = True
            #up
            for k in range(i - 1, -1, -1):
                cur_tree = int(matrix[k][j])
                if cur_tree >= cur: select = False; break
            if select: total += 1; continue
            
            select = True
            #down
            for k in range(i + 1, len(matrix)):
                cur_tree = int(matrix[k][j])
                if cur_tree >= cur: select = False; break
            if select: total += 1; continue
            
            select = True
            #left
            for l in range(j - 1, -1, -1):
                cur_tree = int(matrix[i][l])
                if cur_tree >= cur: select = False; break
            if select: total += 1; continue           
            
            select = True
            #right
            for l in range(j + 1, len(matrix)):
                cur_tree = int(matrix[i][l])
                if cur_tree >= cur: select = False; break
            if select: total += 1; continue  
            
    return total     

    
def p2(lines):
    matrix = [[el.strip() for el in row] for row in lines]
    for i in range(len(matrix) - 1): matrix[i].pop()
    highest = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            
            cur = int(matrix[i][j])
            up = down = left = right = 0

            #up
            for k in range(i - 1, -1, -1):
                up += 1
                if int(matrix[k][j]) >= cur: break
            
            #down
            for k in range(i + 1, len(matrix)):
                down += 1
                if int(matrix[k][j]) >= cur: break
            
            #left
            for l in range(j - 1, -1, -1):
                left += 1
                if int(matrix[i][l]) >= cur: break
            
            #right
            for l in range(j + 1, len(matrix)):
                right += 1
                if int(matrix[i][l]) >= cur: break
            
            highest = max(highest, up * down * left * right)
            
    return highest

print(f'Part 1: {p1(lines)}')
print(f'Part 2: {p2(lines)}')
