import database_creator_x_2000 as databaser
db = databaser.generate_db()
import td_learning as p2
import human_player as p1
import random
'''Administratörfil. Generear listan på non-isomorphic bräden
och låter olika spelare välja drag'''

def find_afterstates(state):
    afterstates = []
    for pointer in db[state[0]].pointers:
        if pointer > state[2]:
            afterstates.append((state[1],state[2],pointer))
        elif pointer < state[1]:
            afterstates.append((pointer,state[1],state[2]))
        else:
            afterstates.append((state[1],pointer,state[2]))
            
    if state[1] != state[0]:
        for pointer in db[state[1]].pointers:
            if pointer > state[2]:
                afterstates.append((state[0],state[2],pointer))
            elif pointer < state[0]:
                afterstates.append((pointer,state[0],state[2]))
            else:
                afterstates.append((state[0],pointer,state[2]))
                
    if state[2] != state[1] and state[2] != state[0]:
        for pointer in db[state[2]].pointers:
            if pointer > state[1]:
                afterstates.append((state[0],state[1],pointer))
            elif pointer < state[0]:
                afterstates.append((pointer,state[0],state[1]))
            else:
                afterstates.append((state[0],pointer,state[1]))
    return afterstates

def run_game():
    current = (0,0,0)
    winner = 1
    while current != (12,12,12):
        current = p1.choice(find_afterstates(current),current)
        if current == (12,12,12):
            winner = 2
            break
        current = p2.choice(find_afterstates(current))
    if winner == 1:
        p1.game_win(True)
        p2.game_win(False)
    else:
        p1.game_win(False)
        p2.game_win(True)
    return winner
def run_games(number):
    stats = []
    for i in range(number):
        stats.append(run_game())
    p1.end()
    p2.end()
    return stats
def countwins(games):
    player1 = 0
    player2 = 0
    for game in games:
        if game == 1:
            player1 += 1
        if game == 2:
            player2 += 1
    return (player1,player2)
print(countwins(run_games(100000)))

    
        
