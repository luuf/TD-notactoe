'''TD-learning AI'''
import pickle
import math
import random
import copy
l = 0.5
temp = 0.01
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
                if policy == "learning" or policy == "tracking":
                    playedmoves.append(states[index])
                return states[index]
def getpmove():
    return savemoves
    
def game_win(win):
    if policy == "learning" or policy == "tracking":
        global playedmoves
        if policy == "tracking":
            global savemoves
            savemoves = [pullstate(i) for i in playedmoves]
        if win:
            score = 1
        else:
            score = 0
        for state in reversed(playedmoves):
            v = pullstate(state)
            score = v+l*(score - v)
            setstate(state,score)
        
        if policy == "tracking":
            savemoves = [(i,savemoves[n],pullstate(i)) for n,i in enumerate(playedmoves)]
        playedmoves = []
    
def end():
    storedata()
db = getdata() #db[0][0][0] ger värdet för state(0,0,0)
