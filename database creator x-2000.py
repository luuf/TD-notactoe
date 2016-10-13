#Database Generator 2000-X9
import copy
class bräde:
    def __init__(self,lista,idnum):
        self.pointers = []
        self.bräde = lista
        self.idnum = idnum
    def add_pointer(self,idnum):
        if idnum not in self.pointers:
            self.pointers.append(idnum)
def rotate(bräde):
    newboard = [[0,0,0],[0,0,0],[0,0,0]]
    for x,list in enumerate(bräde):
        for y,value in enumerate(list):
            newboard[2-y][x] = value
    return newboard
def mirror(bräde):
    newboard = copy.deepcopy(bräde)
    newboard[0],newboard[2] = newboard[2],newboard[0]
    return newboard
def compare(bräde1,bräde2):
    b1 = copy.deepcopy(bräde1)
    b2 = bräde2
    for num in range(0,2):
        for num in range(0,4):
            if b1==b2:
                return True
            b1 = rotate(b1)
        b1 = mirror(b1)
    return False
def find_board_id(bräde):
    for obj in bräden:
        if compare(bräde,obj.bräde):
            return obj.idnum
    return -1
        
        
Brädeninit = [[[0,0,0],[0,0,0],[0,0,0]],
              [[0,0,1],[0,0,0],[0,0,0]],
              [[0,0,0],[0,0,1],[0,0,0]],
              [[0,0,0],[0,1,0],[0,0,0]],
              [[0,0,1],[0,0,1],[0,0,0]],
              [[0,0,1],[0,0,0],[0,0,1]],
              [[0,0,1],[0,1,0],[0,0,0]],
              [[0,0,1],[0,0,0],[0,0,1]],
              [[0,0,1],[0,0,0],[1,0,0]],
              [[0,1,0],[0,0,1],[0,0,0]],
              [[0,0,0],[0,1,1],[0,0,0]],
              [[0,0,0],[1,0,1],[0,0,0]],
              [[0,0,1],[0,0,1],[0,0,1]],
              [[0,1,1],[0,0,1],[0,0,0]],
              [[0,0,1],[0,1,1],[0,0,0]],
              [[0,0,1],[0,0,1],[0,1,0]],
              [[1,0,1],[0,0,1],[0,0,0]],
              [[0,0,1],[0,0,1],[1,0,0]],
              [[0,0,1],[0,1,0],[0,0,1]],
              [[1,0,1],[0,0,0],[0,0,1]],
              [[0,0,1],[1,0,0],[0,0,1]],
              [[0,0,1],[0,1,0],[0,1,0]],
              [[0,0,1],[0,1,0],[1,0,0]],
              [[0,0,1],[1,0,0],[0,1,0]],
              [[0,1,0],[0,1,1],[0,0,0]],
              [[0,0,0],[1,1,1],[0,0,0]],
              [[0,1,1],[0,0,1],[0,0,1]],
              [[0,0,1],[0,1,1],[0,0,1]],
              [[1,0,1],[0,0,1],[0,0,1]],
              [[0,0,1],[1,0,1],[0,0,1]],
              [[0,1,1],[0,1,1],[0,0,0]],
              [[0,1,1],[0,0,1],[0,1,0]],
              [[0,1,1],[0,0,1],[0,1,0]],
              [[0,1,1],[0,0,1],[1,0,0]],
              [[1,0,1],[0,1,1],[0,0,0]],
              [[0,0,1],[1,1,1],[0,0,0]],
              [[0,0,1],[0,1,1],[1,0,0]],
              [[1,0,1],[0,0,1],[0,1,0]],
              [[0,0,1],[1,0,1],[0,1,0]],
              [[0,0,1],[0,0,1],[1,1,0]],
              [[1,0,1],[1,0,1],[0,0,0]],
              [[1,0,1],[0,0,1],[1,0,0]],
              [[1,0,1],[0,1,0],[0,0,1]],
              [[0,0,1],[1,1,0],[0,0,1]],
              [[1,0,1],[0,0,0],[1,0,1]],
              [[0,0,1],[1,1,0],[0,1,0]],
              [[0,1,0],[0,1,1],[0,1,0]],
              [[0,1,0],[1,0,1],[0,1,0]],
              [[0,1,1],[0,1,1],[0,0,1]],
              [[0,1,1],[0,0,1],[0,1,1]],
              [[0,1,1],[1,0,1],[0,0,1]],
              [[0,1,1],[0,0,1],[1,0,1]],
              [[1,0,1],[0,1,1],[0,0,1]],
              [[0,0,1],[1,1,1],[0,0,1]],
              [[1,0,1],[1,0,1],[0,0,1]],
              [[1,0,1],[0,0,1],[1,0,1]],
              [[0,1,1],[0,1,1],[0,1,0]],
              [[0,1,1],[0,1,1],[1,0,0]],
              [[0,1,1],[0,0,0],[0,0,0]],
              [[0,0,0],[0,0,0],[0,0,0]],
              [[0,0,0],[0,0,0],[0,0,0]],
              [[0,0,0],[0,0,0],[0,0,0]]]
bräden = []
for pos,board in enumerate(Brädeninit):
    bräden.append(bräde(board,pos))
for obj in bräden:
    for column,columnlist in enumerate(obj.bräde):
        for position,value in enumerate(columnlist):
            if value == 0:
                copybräde = copy.deepcopy(obj.bräde)
                copybräde[column][position] = 1
                idmatch = find_board_id(copybräde)
                if idmatch != -1:
                    #print("Lade till pointer till " + str(obj.idnum) + ", som pekar mot " + str(idmatch))
                    obj.add_pointer(idmatch)
for obj in bräden:
    print(obj.idnum)
    print("Kan gå till: ")
    print(obj.pointers)
    print("\n")
