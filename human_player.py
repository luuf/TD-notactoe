'''Human Player'''
import database_creator_x_2000 as databaser
db = databaser.generate_db()
current_boards = [[[0,0,0],[0,0,0],[0,0,0]],
                 [[0,0,0],[0,0,0],[0,0,0]],
                 [[0,0,0],[0,0,0],[0,0,0]]]
def boards_to_state(board,sort = True):
    state = []
    for i in range(3):
        state.append(databaser.find_board_id([board[0][i],board[1][i],board[2][i]],db))
    if sort == True:
        return tuple(sorted(state))
    else:
        return tuple(state)
def state_to_board(state,boards):
    if state == (0,0,0):
        return boards
    for x,row in enumerate(boards):
        for y,sub_row in enumerate(row):
            for z,position in enumerate(sub_row):
                if position == 0:
                    boards[x][y][z] = 1
                    if boards_to_state(boards) == state:
                        return boards
                    boards[x][y][z] = 0
    print("ERRRORORORORRO")
def printboards(boards):
    string = ""
    for row in boards:
        for sub_row in row:
            for position in sub_row:
                if position == 1:
                    string += "[X]"
                else:
                    string += "[ ]"
            string += " "
        string += "\n"
    print(string)
def get_input():
    not_correct = True
    while not_correct:
        i = input("Välj var du vil spela, i formatet: bräde,rad,kolumn")
        i = i.split(',')
        if str(0) in i:
            print("0 är inte en giltig siffra, välj 1,2 eller 3")
            continue
        try:
            if current_boards[int(i[0])-1][int(i[1])-1][int(i[2])-1] == 0 and boards_to_state(current_boards,sort = False)[int(i[0])-1] != 12:
                not_correct = False
            else:
                print("Plats ej giltig, försök igen") 
        except (TypeError, ValueError):
            print("Felaktig formattering - det ska vara ex. 1,1,3 för bräde 1, rad 1, kolumn 3 - försök igen. ")
        except IndexError:
            print("Felaktig siffra. Det finns endast 3 bräden, rader och kolumner. Välj 1,2 eller 3 för varje")
    return i
    
def choice(lista,current):
    global current_boards
    current_boards = state_to_board(current,current_boards)
    if current != (0,0,0):
        print("\nMotståndarens drag:")
    else:
        print("\nBrädets utgångsposition:")
    printboards(current_boards)
    i = get_input()
    current_boards[int(i[1])-1][int(i[0])-1][int(i[2])-1] = 1
    print("\nDitt drag var:")
    printboards(current_boards)
    return boards_to_state(current_boards)
def end():
    pass
def game_win(win):
    if win:
        print('You win!')
    else:
        print('You lose!')
