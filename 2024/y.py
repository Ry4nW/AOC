data = [x.rstrip() for x in open("input.txt").readlines()]

def rest(li):
    ret = []
    for l in li:
        c = list(map(int, l.split(',')))
        ret.append(c)
    return ret

rules = []
updates = []

for i in range(len(data)):
    cur = data[i]
    if cur == "": 
        updates = rest(data[i+1:])
        break
    else: rules.append(tuple(map(int, cur.split('|'))))

re = 0
rules = sorted(rules, key=lambda x: x[0])
for up in updates:
    p_to_i = { x[1]:x[0] for x in enumerate(up) }
    nr = list(filter(lambda x: x[1] in up and x[0] in up, rules))
    print(nr)
    b=False
    for _ in range(len(nr)):
        for rule in nr:
            r0 = rule[0];  r1=rule[1]

            r0_i = p_to_i[r0];r1_i = p_to_i[r1]
            if r0_i > r1_i: 
                up[r0_i], up[r1_i] = up[r1_i], up[r0_i]
                p_to_i[r0] = r1_i
                p_to_i[r1] = r0_i
                b = True

    if b: re += up[len(up)//2]
print(re)

'''
97,13,29,75,47
97,13,75,29,47
97,13,47,29,75
97,13,47,75,29

97,13,29,47,75
97,13,75,47,29
97,13,47,75,29
97,13,47,75,29

47|75
75|29

'''
