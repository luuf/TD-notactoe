'''TD-learning AI'''
import pickle
import math
import random
l = 0.5
temp = 0.2
playedmoves = []
policy = "learning"
def getdata():
    try:
        return pickle.load(open("db.dat","rb"))
    except:
        return resetdata()
def storedata():
    pickle.dump(db,open("db.dat","wb"),pickle.HIGHEST_PROTOCOL)
def resetdata():
    return [[[0.5 for i in range(47)] for j in range(47)] for k in range(47)]              
def pullstate(state):
    return db[state[0]][state[1]][state[2]]
def setstate(state,value):
    db[state[0]][state[1]][state[2]] = value
    
def choice(states,current):
    if policy == "final":
        return max(states, key=lambda x:db[x[0]][x[1]][x[2]])
    else:
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
                if policy == "learning":
                    playedmoves.append(states[index])
                return states[index]

def game_win(win):
    if policy == "learning":
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
