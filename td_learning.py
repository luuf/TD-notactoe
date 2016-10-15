'''TD-learning AI'''
import pickle
import math
import random
l = 0.5
temp = 0.1
playedmoves = []
def getdata():
    return pickle.load(open("db.dat","rb"))
def storedata():
    pickle.dump(db,open("db.dat","wb"),pickle.HIGHEST_PROTOCOL)
def resetdata():
    return [[[0.5 for i in range(47)] for j in range(47)] for k in range(47)]              
def pullstate(state):
    return db[state[0]][state[1]][state[2]]
def setstate(state,value):
    db[state[0]][state[1]][state[2]] = value
    
def choice(states):
    global playedmoves
    scores = []
    for state in states:
        scores.append((math.e)**(pullstate(state)/temp))
    sumscores = sum(scores)
    num = random.random()
    for index,score in enumerate(scores):
        if score/sumscores < num:
            num = num - score/sumscores
        else:
            playedmoves.append(states[index])
            return states[index]

def game_win(win):
    global playedmoves
    if win:
        previous_score = 1
    else:
        previous_score = 0
    for state in reversed(playedmoves):
        v = pullstate(state)
        previous_score = v+l*(previous_score - v)
        setstate(state,previous_score)
    playedmoves = []
    
def end():
    storedata()
db = getdata() #db[0][0][0] ger värdet för state(0,0,0)
db = resetdata()
