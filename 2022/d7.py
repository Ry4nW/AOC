# needs fixing

f1 = open('./input/d7.txt', 'r')
lines = f1.readlines()


class Direc:
    def __init__(self, name):
        self.direcs = []
        self.files = []
        self.name = name
        self.prev = None
    
    def get_direcs(self): return self.direcs
    
    def add_direc(self, direc): self.direcs.append(direc)
    def add_file(self, file): self.files.append(file)
    
    def __repr__(self): return self.name
    
    
class FileStructure:
    def __init__(self) -> None:
        self.root = Direc('/')
        self.depth = 1
        self.nodes = 1
        
    def get_direc(self, path):
        cur_direc = self.root
        depth = 0
        while depth < len(path) - 1:
            found = False
            for direc in cur_direc.direcs:
                if direc.name == path[depth]:
                    cur_direc = direc
                    depth += 1 
                    if depth > self.depth: self.depth += 1
                    found = True
                    break
                
            if not found: return None
        return cur_direc
        
    # def insert_direc(self, path, direc:Direc):
    #     cur_direc = self.get_direc(path)
    #     cur_direc.add_direc(direc)
        
    #     if len(path) > 0: direc.prev = path[-1]
    #     else: cur_direc.prev = self.root
    

fs = FileStructure()
size_count = {'/':0}
glo_direc = []

def parse(cmd:str):
    global glo_direc
    work_direc = fs.get_direc(glo_direc)
    if work_direc == None: return
    cmd = cmd.split()
    cur = cmd[0]
    instruc = cmd[1]

    if instruc == 'cd':
        cur_direc = cmd[2]
        if cur_direc == '/': glo_direc = []
        elif cur_direc == '..': 
            if len(glo_direc) > 0: glo_direc.pop()
        else: glo_direc.append(cur_direc)
        
    elif cur == 'dir':
        if instruc not in [d.name for d in work_direc.get_direcs()]:
            work_direc.add_direc(Direc(instruc))
            fs.nodes += 1
            size_count['/'.join(glo_direc) + '/' + instruc] = 0
            
    elif cur.isdigit():
        cur = int(cur)
        work_direc.add_file(cur)
        try:
            size_count['/' + '/'.join(glo_direc)] += cur
        except:
            size_count['/'.join(glo_direc)] += cur
        

def p1(lines):
    for command in lines:
        parse(command)
    
    total = 0
    for direc in size_count:
        cur = size_count[direc]
        if cur <= 100000: total += cur
    
    return total

    
def p2(lines):
    pass

print(f'Part 1: {p1(lines)}')
print(f'Part 2: {p2(lines)}')
