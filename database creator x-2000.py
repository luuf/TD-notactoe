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
def isdead(bräde):
    if (bräde[0][0] and bräde[0][1] and bräde[0][2]) or (bräde[1][0] and bräde[1][1] and bräde[1][2]) or (bräde[2][0] and bräde[2][1] and bräde[2][2]) or (bräde[0][0] and bräde[1][0] and bräde[2][0]) or (bräde[0][1] and bräde[1][1] and bräde[2][1]) or (bräde[0][2] and bräde[1][2] and bräde[2][2]) or (bräde[0][0] and bräde[1][1] and bräde[2][2]) or (bräde[0][2] and bräde[1][1] and bräde[2][0]):
        return True
    else:
        return False
def printboard(bräde):
    string = ""
    for row in [[bräde[0][2],bräde[1][2],bräde[2][2]],
                  [bräde[0][1],bräde[1][1],bräde[2][1]],
                  [bräde[0][0],bräde[1][0],bräde[2][0]]]:
        for value in row:
            if value == 1:
                string += "[X]"
            if value == 0:
                string += "[ ]"
        string += "\n"
    print(string)
            
        
        
Brädeninit = [[[0,0,0],[0,0,0],[0,0,0]],
              [[0,0,1],[0,0,0],[0,0,0]],
              [[0,0,0],[0,0,1],[0,0,0]],
              [[0,0,0],[0,1,0],[0,0,0]],
              [[0,0,1],[0,0,1],[0,0,0]],
              [[0,0,1],[0,0,0],[0,0,1]],
              [[0,0,1],[0,1,0],[0,0,0]],
              [[0,0,1],[0,0,0],[0,1,0]],
              [[0,0,1],[0,0,0],[1,0,0]],
              [[0,1,0],[0,0,1],[0,0,0]],
              [[0,0,0],[0,1,1],[0,0,0]],
              [[0,0,0],[1,0,1],[0,0,0]],
              [[0,0,1],[0,0,1],[0,0,1]],
              [[0,1,1],[0,0,1],[0,0,0]],
              [[0,0,1],[0,1,1],[0,0,0]],
              [[0,0,1],[0,0,1],[0,1,0]],
              [[1,0,1],[0,0,1],[0,0,0]],
              [[0,0,1],[1,0,1],[0,0,0]],
              [[0,0,1],[0,0,1],[1,0,0]],
              [[0,0,1],[0,1,0],[0,0,1]],
              [[1,0,1],[0,0,0],[0,0,1]],
              [[0,0,1],[1,0,0],[0,0,1]],
              [[0,0,1],[0,1,0],[0,1,0]],
              [[0,0,1],[0,1,0],[1,0,0]],
              [[0,0,1],[1,0,0],[0,1,0]],
              [[0,1,0],[0,1,1],[0,0,0]],
              [[0,1,0],[0,0,1],[0,1,0]],
              [[0,0,0],[1,1,1],[0,0,0]],
              [[0,1,1],[0,0,1],[0,0,1]],
              [[0,0,1],[0,1,1],[0,0,1]],
              [[1,0,1],[0,0,1],[0,0,1]],
              [[0,0,1],[1,0,1],[0,0,1]],
              [[0,1,1],[0,1,1],[0,0,0]],
              [[0,1,1],[0,0,1],[0,1,0]],
              [[0,1,1],[0,0,1],[1,0,0]],
              [[0,0,1],[0,1,1],[0,1,0]],
              [[1,0,1],[0,1,1],[0,0,0]],
              [[0,0,1],[1,1,1],[0,0,0]],
              [[0,0,1],[0,1,1],[1,0,0]],
              [[1,0,1],[0,0,1],[0,1,0]],
              [[0,0,1],[1,0,1],[0,1,0]],
              [[0,0,1],[0,0,1],[1,1,0]],
              [[1,0,1],[1,0,1],[0,0,0]],
              [[1,0,1],[0,0,1],[1,0,0]],
              [[0,0,1],[1,0,1],[1,0,0]],
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
              [[0,1,1],[1,0,1],[0,1,0]],
              [[0,1,1],[0,0,1],[1,1,0]],
              [[1,0,1],[0,1,1],[0,1,0]],
              [[1,0,1],[1,0,1],[0,1,0]],
              [[1,0,1],[0,0,1],[1,1,0]],
              [[0,1,1],[1,0,1],[1,1,0]],
              [[1,1,1],[1,1,1],[1,1,1]]]
bräden = []
added_dead = False
index = 0
for board in Brädeninit:
    if isdead(board):
        if not added_dead:
            added_dead = True
            bräden.append(bräde(board,index))
            index += 1
    else:
        bräden.append(bräde(board,index))
        index += 1
for obj in bräden:
    for column,columnlist in enumerate(obj.bräde):
        for position,value in enumerate(columnlist):
            if value == 0:
                copybräde = copy.deepcopy(obj.bräde)
                copybräde[column][position] = 1
                if isdead(copybräde):
                    obj.add_pointer(12)
                else:
                    idmatch = find_board_id(copybräde)
                    if idmatch != -1:
                        obj.add_pointer(idmatch)
for obj in bräden:
    
    print(obj.idnum)
    printboard(obj.bräde)
    print("Kan gå till: ")
    print(obj.pointers)
    print("\n")
#hej
