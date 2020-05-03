BOARD_WIDTH = 3
BOARD_HEIGHT = 3
player1 = 'X'
player2 = 'Y'

def new_board():
    
    board = []
    
    for i in range (BOARD_WIDTH):
        col = []
        for j in range (BOARD_HEIGHT):
            col.append(None)
        board.append(col)

    return board

def render(board):
    rows = []
    for y in range(0, BOARD_HEIGHT):
        row = []
        for x in range(0, BOARD_WIDTH):
            row.append(board[x][y])
        rows.append(row)

    row_num = 0
    print('  0 1 2 ')
    print('  ------')
    for row in rows:
        output_row = ''
        for sq in row:
            if sq is None:
                output_row += ' '
            else:
                output_row += sq
        print("%d|%s|" % (row_num, ' '.join(output_row)))
        row_num += 1
    print('  ------')

def get_move():
    coords = []
    print('X coord: ')
    coords.append(int(input()))
    print('Y coord: ')
    coords.append(int(input()))

    return coords

def make_move(board, coords, player):
    x = coords[0]
    y = coords[1]
    board[x][y] = player

    return board

def get_player_turn(turnCount):
    if turnCount % 2 == 0:
        return player1
    else: return player2


def is_valid(board, coords):
    x = coords[0]
    y = coords[1]
    l = [0, 1, 2]

    if(x in l and y in l and board[x][y] == None):
        return True
    else: return False

def play():

    turnCount = 0
    board = new_board()    

    while True:
        render(board)
        coords = get_move()

        while True:
            if is_valid(board, coords) == True:
                board = make_move(board, coords, get_player_turn)
                break

            else:
                print('invalid move try again')
                coords = get_move()
        turnCount = turnCount + 1

play()


