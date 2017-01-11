import database_creator_x_2000 as databaser
import pylab as plab
import pickle
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
def printstate(state):
    databaser.printboard(db[state[0]].bräde)
    databaser.printboard(db[state[1]].bräde)
    databaser.printboard(db[state[2]].bräde)
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
def plot_winrate(stats,x_size = 1200,y_size = 800,xlabelmod = 1,x_start = 0):
    for statlist in stats:
        if len(statlist) != len(stats[0]):
            print("Alla listor måste vara lika långa!!")
            return 0
    x = [0+x_start,len(stats[0])*xlabelmod+x_start-1]
    y = [0.9,0.9]
    x_list = []
    for number in range(len(stats[0])):
        x_list.append(x_start + number*xlabelmod)
    plab.figure(figsize=(x_size/128,y_size/128), dpi = 128)
    for statlist in stats:
        plab.plot(x_list,statlist)
    plab.plot(x,y)
    plab.xlabel('Learning Games')
    plab.ylabel('Winrate')
    plab.title('Learning Results')
    axes = plab.gca()
    axes.set_ylim([0,1])
    plab.savefig("LearningGraph.png")
    plab.show()
def learning_session(games,player,learning_games,x_size = 1200,temp = 0.05,track = [],passivetrack = True):
    trackedstates = []
    changes = []
    for state in track:
        trackedstates.append([state,[]])
    if learning_games > x_size:
        if learning_games%x_size != 0:
            print("learning games needs to be multiple of " + str(x_size))
            return 0
        else:
            games_per_x = learning_games//x_size
    if player == 1:
        p1.temp = temp
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
            if passivetrack:
                p1.policy = "tracking"
            else:
                p1.policy = "learning"
            run_game()
            if passivetrack:
                changes.append(p1.getpmove())
            for index,state in enumerate(track):
                trackedstates[index][1].append(p1.pullstate(state))
    if player == 2:
        p2.temp = temp
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
            if passivetrack:
                p1.policy = "tracking"
            else:
                p1.policy = "learning"
            run_game()
            if passivetrack:
                changes.append(p2.getpmove())
            for index,state in enumerate(track):
                trackedstates[index][1].append(p1.pullstate(state))
    if learning_games > x_size:
        win_rates_adjusted = []
        for index in range(0,len(win_rates),games_per_x):
            tot = 0
            for sak in range(games_per_x):
                tot += win_rates[index + sak]
            win_rates_adjusted.append(tot/games_per_x)
    else:
        win_rates_adjusted = win_rates
        games_per_x = 1
    return (win_rates_adjusted,games_per_x,trackedstates,changes)
def plot_learning(games,player,learning_games,x = 1200,temp = 0.05):
    """Kör en learning_session och plottar den"""
    learning_tuple = learning_session(games,player,learning_games,x,temp = temp)
    stat = learning_tuple[0]
    games_per_x = learning_tuple[1]
    plot_winrate([stat],x_size = x,xlabelmod = games_per_x)
def average_runs(runs,games,player,learning_games,x_size = 1200,temp = 0.05):
    values = learning_session(games,player,learning_games,x_size,temp, passivetrack = False)
    games_per_x = values[1]
    averaged_list = plab.array(values[0])
    for run in range(runs-1):
        averaged_list += plab.array(learning_session(games,player,learning_games,x_size,temp, passivetrack = False)[0])
    averaged_list = averaged_list/(runs)
    return (averaged_list,games_per_x)
def picklestats(stats,name):
    pickle.dump(stats,open(name,"wb"),pickle.HIGHEST_PROTOCOL)
def getstats(name):
    return pickle.load(open(name,"rb"))
        
