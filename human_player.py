'''Human Player'''
import random
import database_creator_x_2000 as databaser
db = databaser.generate_db()
current_boards = [[[0,0,0],[0,0,0],[0,0,0]],
          [[0,0,0],[0,0,0],[0,0,0]],
          [[0,0,0],[0,0,0],[0,0,0]]]
def boards_to_state(board):
    state = []
    for i in range(3):
        state.append(databaser.find_board_id([board[0][i],board[1][i],board[2][i]],db))
    return tuple(sorted(state))
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
                
def choice(lista,current):
    global current_boards
    current_boards = state_to_board(current,current_boards)
    printboards(current_boards)
    i = input("bräde,rad,kolumn")
    i = i.split(',')
    current_boards[int(i[1])-1][int(i[0])-1][int(i[2])-1] = 1
    printboards(current_boards)
    return boards_to_state(current_boards)
def end():
    pass
def game_win(win):
    if win:
        print('You win!')
    else:
        print('You lose!')
