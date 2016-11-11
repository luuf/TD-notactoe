import database_creator_x_2000 as databaser
import pylab as plab
db = databaser.generate_db()
i = input('p1p2: t för ai, r för random, h för human, p för perfect \n')
if i[0] == 't':
    import td_learning as p1
elif i[0] == 'h':
    import human_player as p1
elif i[0] == 'p':
    import perfect_player as p1
else:
    import random_player as p1
if i[-1] == 't':
    import td_learning as p2
elif i[-1] == 'h':
    import human_player as p2
elif i[-1] == 'p':
    import perfect_player as p2
else:
    import random_player as p2
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
        current = p2.choice(find_afterstates(current),current)
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
def plot_winrate(stats,x_size = 1200,y_size = 800):
    x = [0,len(stats)]
    y = [0.9,0.9]
    plab.figure(figsize=(x_size/128,y_size/128), dpi = 128)
    plab.plot(stats)
    plab.plot(x,y)
    plab.xlabel('Learning Games')
    plab.ylabel('Winrate')
    plab.title('Learning Results')
    plab.savefig("LearningGraph.png")
    axes = plab.gca()
    axes.set_ylim([0,1])
    plab.show()
def plottdlearning(games,player,learning_games):
    if player == 1:
        p1.db = p1.resetdata()
        p1.storedata()
        win_rates=[]
        for i in range(learning_games):
            wins = 0
            p1.policy = "blank"
            for j in range(games):
                if run_game() == 1:
                    wins += 1
            win_rates.append(wins/games)
            p1.policy = "learning"
            run_game()
    if player == 2:
        p2.db = p2.resetdata()
        p2.storedata()
        win_rates=[]
        for i in range(learning_games):
            wins = 0
            p2.policy = "blank"
            for j in range(games-1):
                if run_game() == 2:
                    wins += 1
            win_rates.append(wins/games)
            p2.policy = "learning"
            run_game()
    plot_winrate(win_rates)
    
    
        
#print(countwins(run_games(1000)))

    
        
