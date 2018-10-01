#CSCI 1133 Homework 3
#Peiqi Ji
#Problem D
def check(m,board):
    if board[m//3][m%3] != ' ':
        return True
    else:
        return False
def win(board):
    for x in board:
        if x[0] == x[1] and x[1] == x[2]:
            if x[0] == 'x':
                return 'x'
            elif x[0] == 'o':
                return 'o'
    for y in range(0,3):
        if board[0][y] == board[1][y] and board[1][y] == board[2][y]:
            if board[0][y] == 'x':
                return 'x'
            elif board[0][y] == 'o':
                return 'o'
    if  board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 'x':
            return 'x'
        elif board[0][0] == 'o':
            return 'o'
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == 'x':
            return 'x'
        elif board[0][2] == 'o':
            return 'o'
    return 't'
def move(player,position,board):
    if player == 'x':
        board[position//3][position%3] = 'x'
    if player == 'o':
        board[position//3][position%3] = 'o'
    return board
def robat(board):
    if board[1][1] == ' ':
        board[1][1] = 'o'
        return board
    elif board[0][0] == board[1][1] and board[2][2] == ' ':
        board[2][2] = 'o'
        return board
    elif board[2][2] == board[1][1] and board[0][0] == ' ':
        board[0][0] = 'o'
        return board
    elif board[0][2] == board[1][1] and board[2][0] == ' ':
        board[2][0] = 'o'
        return board
    elif board[2][0] == board[1][1] and board[0][2] == ' ':
        board[2][0] = 'o'
        return board
    for x in range(0,3):
        if board[0][x] == board[1][x] and board[2][x] == ' ':
            board[2][x] = 'o'
            return board
        elif board[x][0] == board[x][1] and board[x][2] == ' ':
            board[x][2] = 'o'
            return board
    for z in range(0,3):
        for h in range(0,3):
            if board[z][h] == ' ':
                board[z][h] = 'o'
                return board
def main():
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    print('Welcome to the world of Tic Tac Toe!')
    i = 0
    while i < 9:
        m1 = int(input(' where would you like to move? '))
        while check(m1,board):
            print('Sorry, that space is already taken.')
            for lines in board:
                print(lines)
            m1 = int(input(' where would you like to move? '))
        board = move('x',m1,board)
        for lines in board:
            print(lines)
        i += 1
        if i == 9 :
            break
        if win(board) == 'x':
            print('You wins!')
            break
        print("It's time for my turn")
        board = robat(board)
        for lines in board:
            print(lines)
        i += 1
        if win(board) == 'o':
            print(' You lose!')
            break
    if win(board) == 't':
        print('No one wins!')
if __name__ == '__main__':
    main()
