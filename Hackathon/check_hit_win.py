import random
list_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
list_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
let_to_num = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7, 'I':8} 

  
def player_turn(board, name): 
    guess_empty = False
    while guess_empty == False:
        try:
            ply_guess_r = int(input('Enter the row: ')) 
            while ply_guess_r not in list_row:
                ply_guess_r = int(input('You have to enter a number from 1 to 9 ')) 
        except ValueError:
            ply_guess_r = int(input('You have to enter a number from 1 to 9 '))
            
        ply_guess_c = input('Enter the column: ').upper()
        while ply_guess_c not in list_column:
            ply_guess_c = input('You have to enter a letter from A to I ').upper()
            
        ply_guess_r -= 1
        ply_guess_c_idx = let_to_num[ply_guess_c]
        
        if board[ply_guess_r][ply_guess_c_idx] == '_':
            board[ply_guess_r][ply_guess_c_idx] = '-'
            print(f'{name} launched a missile at place: {ply_guess_r + 1}, {ply_guess_c}')
            guess_empty = True
        else:
            print('You already guessed this spot')
            
    return (ply_guess_r, ply_guess_c_idx)

def comp_turn_fisrt_guess(board, name):
    while True:
        com_guess_r, com_guess_c = random.randint(0, 8), random.choice(list_column)
        com_guess_c_idx = let_to_num[com_guess_c]
        if board[com_guess_r][com_guess_c_idx] == '_':
            board[com_guess_r][com_guess_c_idx] = '-'
            print(f'{name} launched a missile at place: {com_guess_r + 1}, {com_guess_c}')
            return (com_guess_r, com_guess_c_idx)


def com_turn_check_around(board, com_pos, name):
    around_possibilities = []
    r, c = com_pos
    if r - 1 >= 0 and board[r - 1][c] == '_':
        around_possibilities.append((r - 1, c))
    if c + 1 < 9 and board[r][c + 1] == '_':
        around_possibilities.append((r, c + 1))
    if r + 1 < 9 and board[r + 1][c] == '_':
        around_possibilities.append((r + 1, c))
    if c - 1 >= 0 and board[r][c - 1] == '_':
        around_possibilities.append((r, c - 1))
        
    com_try_around = random.choice(around_possibilities)
    try_r, try_c = com_try_around
    board[try_r][try_c] = '-'
    
    for key, val in let_to_num.items():
        if val == try_c:
            try_c_let = key
            break 
        
    print(f'{name} launched a missile at place: {try_r + 1}, {try_c_let}')

    return (try_r, try_c)


def check_hit(board_ply, board2, ply_pos, name):
    good_guesses = []
    r, c = ply_pos
    if board2[r][c] != '_':
        print(f'{name} hit a ship!')
        board_ply[r][c] = '*'
        good_guesses.append((r, c))
        return good_guesses, True
    else:
        print(f'{name} missed')
        return good_guesses, False
        
    


def chek_if_sank(board, g_guesses, name, list_X: list, list_K: list, list_D: list, list_O: list, list_H: list):
    for pos in g_guesses:
        if board[pos[0]][pos[1]] == 'X':
            list_X.append(pos)
        elif board[pos[0]][pos[1]]== 'K':
            list_K.append(pos)
        elif board[pos[0]][pos[1]] == 'D':
            list_D.append(pos)
        elif board[pos[0]][pos[1]] == 'O':
            list_O.append(pos)
        elif board[pos[0]][pos[1]] == 'H':
            list_H.append(pos)
    
    if len(list_X) == 4:
        print(f'{name} sank the Carrier')
        list_X.clear()
        return 1
    elif len(list_K) == 4:
        print(f'{name} sank the Battleship')
        list_K.clear()
        return 1
    elif len(list_D) == 3:
        print(f'{name} sank the Cruiser')
        list_D.clear()
        return 1
    elif len(list_O) == 2:
        print(f'{name} sank the Submarine')
        list_O.clear()
        return 1
    elif len(list_H) == 2:
        print(f'{name} sank the Destroyer')
        list_H.clear()
        return 1
    else:
        return 0