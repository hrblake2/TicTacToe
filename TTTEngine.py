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

def is_valid(board, coords):
    x = coords[0]
    y = coords[1]

    l = [0, 1, 2]
    
    if(board[x][y] is None and x and y in l):
        print('not a valid move') 
        return False

    else:
        print('valid move') 
        return True