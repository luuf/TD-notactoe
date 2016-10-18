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
    for row in boards:
        for sub_row in row:
            for position in sub_row:
                if position == 0:
                    position = 1
                    print(state)
                    print(boards_to_state(boards))
                    if boards_to_state(boards) == state:
                        return boards
                    position = 0
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
    ilist = i.split(',')
    current_boards[i[1]][i[0]][i[2]] = 1
    return boards_to_state(current_boards)
def end():
    pass
def game_win(win):
    pass
