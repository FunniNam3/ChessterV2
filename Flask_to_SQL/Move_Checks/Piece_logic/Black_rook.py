def Black_rook(position, board, location):
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
    
    # Convert the list of lists(possible_moves) into a more readable format
    for x in range(len(possible_moves)):
        possible_moves[x] = ''.join(possible_moves[x])
    possible_moves = ','.join(possible_moves)
    return possible_moves