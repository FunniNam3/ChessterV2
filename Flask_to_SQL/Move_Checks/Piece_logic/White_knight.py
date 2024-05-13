def White_knight(position, board, location):
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
    # Checks if knight can move in the upward direction
    if(row>1):
        # Check if knight can move up left
        if(column>0):
            # Checks if the square up left is empty
            if(board[row-2][column-1]=='.'):
                # Sets the location as a valid spot to move to
                possible_moves[row-2][column-1] = 'm'
            # Checks if the square up left has a black piece
            if(board[row-2][column-1].islower()):
                # Sets the location as a valid spot to take
                possible_moves[row-2][column-1] = 't'
        # Check if knight can move up right
        if(column<7):
            # Checks if the square up right is empty
            if(board[row-2][column+1]=='.'):
                # Sets the location as a valid spot to move to
                possible_moves[row-2][column+1] = 'm'

            # Checks if the square up right has a black piece
            if(board[row-2][column+1].islower()):
                # Sets the location as a valid spot to take
                possible_moves[row-2][column+1] = 't'
    
    # Checks if knight can move in the downward direction
    if(row<6):
        # Check if knight can move down left
        if(column>0):
            # Checks if the square down left is empty
            if(board[row+2][column-1]=='.'):
                # Sets the location as a valid spot to move to
                possible_moves[row+2][column-1] = 'm'
            # Checks if the square down left has a black piece
            if(board[row+2][column-1].islower()):
                # Sets the location as a valid spot to take
                possible_moves[row+2][column-1] = 't'
        # Check if knight can move down right
        if(column<7):
            # Checks if the square down right is empty
            if(board[row+2][column+1]=='.'):
                # Sets the location as a valid spot to move to
                possible_moves[row+2][column+1] = 'm'

            # Checks if the square down right has a black piece
            if(board[row+2][column+1].islower()):
                # Sets the location as a valid spot to take
                possible_moves[row+2][column+1] = 't'

    # Checks if knight can move in the right direction
    if((column)<6):
        # Check if knight can move right up
        if(row>0):
            # Checks if the square right up is empty
            if(board[row-1][column+2]=='.'):
                # Sets the location as a valid spot to move to
                possible_moves[row-1][column+2] = 'm'
            # Checks if the square right up has a black piece
            if(board[row-1][column+2].islower()):
                # Sets the location as a valid spot to take
                possible_moves[row-1][column+2] = 't'
        # Check if knight can move right down
        if(row<7):
            # Checks if the square right down is empty
            if(board[row+1][column+2]=='.'):
                # Sets the location as a valid spot to move to
                possible_moves[row+1][column+2] = 'm'
            # Checks if the square right down has a black piece
            if(board[row+1][column+2].islower()):
                # Sets the location as a valid spot to take
                possible_moves[row+1][column+2] = 't'
    
    # Checks if knight can move in the left direction
    if((column)>1):
        # Check if knight can move left up
        if(row>0):
            # Checks if the square left up is empty
            if(board[row-1][column-2]=='.'):
                # Sets the location as a valid spot to move to
                possible_moves[row-1][column-2] = 'm'
            # Checks if the square left up has a black piece
            if(board[row-1][column-2].islower()):
                # Sets the location as a valid spot to take
                possible_moves[row-1][column-2] = 't'
        # Check if knight can move left down
        if(row<7):
            # Checks if the square left down is empty
            if(board[row+1][column-2]=='.'):
                # Sets the location as a valid spot to move to
                possible_moves[row+1][column-2] = 'm'
            # Checks if the square left down has a black piece
            if(board[row+1][column-2].islower()):
                # Sets the location as a valid spot to take
                possible_moves[row+1][column-2] = 't'

    # Convert the list of lists(possible_moves) into a more readable format
    for x in range(len(possible_moves)):
        possible_moves[x] = ''.join(possible_moves[x])
    possible_moves = ','.join(possible_moves)
    return possible_moves