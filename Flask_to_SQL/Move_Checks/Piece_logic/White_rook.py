def White_rook(position, board, location):
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
            if board[x][column].islower():
                possible_moves[x][column]='t'
            break
    for x in range(row+1,8):
        if board[x][column]=='.':
            possible_moves[x][column]='m'
        else:
            if board[x][column].islower():
                possible_moves[x][column]='t'
            break
    for x in range(column-1,-1,-1):
        if board[row][x]=='.':
            possible_moves[row][x]='m'
        else:
            if board[row][x].islower():
                possible_moves[row][x]='t'
            break
    for x in range(column+1,8):
        if board[row][x]=='.':
            possible_moves[row][x]='m'
        else:
            if board[row][x].islower():
                possible_moves[row][x]='t'
            break

    # Convert the list of lists(possible_moves) into a more readable format
    for x in range(len(possible_moves)):
        possible_moves[x] = ''.join(possible_moves[x])
    possible_moves = ','.join(possible_moves)
    return possible_moves