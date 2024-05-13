def White_king(position, board, location):
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
    
    # checks row below king
    if(row+1<=7):
        # Loops through the 3 columns above the king
        for x in range(column-1,column+2):
            # checks if the column is within the board
            if(0<=x<=7):
                # Checks if square is empty
                if(board[row+1][x]=='.'):
                    # Sets the square to a possible move
                    possible_moves[row+1][x]='m'
                # Checks if square is an opponent
                if(board[row+1][x].islower()):
                    # Sets the square as a possible take
                    possible_moves[row+1][x]='t'
    # Checks row above king
    if(row-1>=0):
        # Loops through the 3 columns below the king
        for x in range(column-1,column+2):
            # checks if the column is within the board
            if(0<=x<=7):
                # Checks if square is empty
                if(board[row-1][x]=='.'):
                    # Sets the square to a possible move
                    possible_moves[row-1][x]='m'
                # Checks if square is an opponent
                if(board[row-1][x].islower()):
                    # Sets the square as a possible take
                    possible_moves[row-1][x]='t'

    if(column<7):
        # Checks if square is empty
        if(board[row][column+1]=='.'):
            # Sets the square to a possible move
            possible_moves[row][column+1]='m'
        # Checks if square is an opponent
        if(board[row][column+1].islower()):
            # Sets the square as a possible take
            possible_moves[row][column+1]='t'
    if(column>0):
        # Checks if square is empty
        if(board[row][column-1]=='.'):
            # Sets the square to a possible move
            possible_moves[row][column-1]='m'
        # Checks if square is an opponent
        if(board[row][column-1].islower()):
            # Sets the square as a possible take
            possible_moves[row][column-1]='t'

    # Convert the list of lists(possible_moves) into a more readable format
    for x in range(len(possible_moves)):
        possible_moves[x] = ''.join(possible_moves[x])
    possible_moves = ','.join(possible_moves)
    return possible_moves