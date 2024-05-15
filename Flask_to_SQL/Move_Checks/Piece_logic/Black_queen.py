def Black_queen(position, board, location):
    # Creates an list to store the possible moves that a piece can make
    possible_moves=[
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.']
    ]
    # Stores variables for row and column
    column = int(location[1])
    row = int(location[0])

    # Finds the position of the current piece and places it in the 'possible_moves' list for easier debugging
    possible_moves[row][column] = board[row][column]

    # Checks for possible moves
    for x in range(row-1,-1,-1):
        if board[x][column]=='.':
            possible_moves[x][column]='m'
        else:
            if board[x][column].isupper():
                possible_moves[x][column]='t'
            break
    for x in range(row+1,8):
        if board[x][column]=='.':
            possible_moves[x][column]='m'
        else:
            if board[x][column].isupper():
                possible_moves[x][column]='t'
            break
    for x in range(column-1,-1,-1):
        if board[row][x]=='.':
            possible_moves[row][x]='m'
        else:
            if board[row][x].isupper():
                possible_moves[row][x]='t'
            break
    for x in range(column+1,8):
        if board[row][x]=='.':
            possible_moves[row][x]='m'
        else:
            if board[row][x].isupper():
                possible_moves[row][x]='t'
            break
    if row<=column:
        for x in range(row-1,-1,-1):
            if(column+(row-x)>7):
                break
            if board[x][column+(row-x)]=='.':
                possible_moves[x][column+(row-x)]='m'
            else:
                if board[x][column+(row-x)].isupper():
                    possible_moves[x][column+(row-x)]='t'
                break
        for x in range(row-1,-1,-1):
            if(column+(row-x)<0):
                break
            if board[x][column-(row-x)]=='.':
                possible_moves[x][column-(row-x)]='m'
            else:
                if board[x][column-(row-x)].isupper():
                    possible_moves[x][column-(row-x)]='t'
                break
        for x in range(column+1,8):
            if(row+(column-x)>7):
                break
            if board[row+(x-column)][x]=='.':
                possible_moves[row+(x-column)][x]='m'
            else:
                if board[row+(x-column)][x].isupper():
                    possible_moves[row+(x-column)][x]='t'
                break
        for x in range(column-1,-1,-1):
            if(row+(column-x)>7):
                break
            if board[row+(column-x)][x]=='.':
                possible_moves[row+(column-x)][x]='m'
            else:
                if board[row+(column-x)][x].isupper():
                    possible_moves[row+(column-x)][x]='t'
                break
    else:
        for x in range(column-1,-1,-1):
            if(row+(column-x)>7):
                break
            if board[row+(column-x)][x]=='.':
                possible_moves[row+(column-x)][x]='m'
            else:
                if board[row+(column-x)][x].isupper():
                    possible_moves[row+(column-x)][x]='t'
                break
        for x in range(column-1,-1,-1):
            if(row-(column-x)<0):
                break
            if board[row-(column-x)][x]=='.':
                possible_moves[row-(column-x)][x]='m'
            else:
                if board[row-(column-x)][x].isupper():
                    possible_moves[row-(column-x)][x]='t'
                break
        for x in range(row+1,8):
            if(column+(row-x)>7):
                break
            if board[x][column+(x-row)]=='.':
                possible_moves[x][column+(x-row)]='m'
            else:
                if board[x][column+(x-row)].isupper():
                    possible_moves[x][column+(x-row)]='t'
                break
        for x in range(row-1,-1,-1):
            if(column+(row-x)>7):
                break
            if board[x][column+(row-x)]=='.':
                possible_moves[x][column+(row-x)]='m'
            else:
                if board[x][column+(row-x)].isupper():
                    possible_moves[x][column+(row-x)]='t'
                break

    # Convert the list of lists(possible_moves) into a more readable format
    for x in range(len(possible_moves)):
        possible_moves[x] = ''.join(possible_moves[x])
    possible_moves = ','.join(possible_moves)
    return possible_moves