def White_pawn(position, board, location):
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
    # Checks if the pawn can move forward 1 square
    if(row>0):
        # Checks if the square is empty
        if(board[row-1][column]=='.'):
            # Sets the location as a valid spot to move to
            possible_moves[row-1][column] = 'm'
            # Checks if the pawn can move forward 2 squares and has not moved yet
            if((row)==6 and board[row-2][column]=='.'):
                # Sets the location as a valid spot to move to
                possible_moves[row-2][column] = 'm'

    # Checks for possible takes
    # Checks if its possible to even move forward
    if(row>0):
        # Checks if possible to move left
        if(column>0):
            # Checks if the location is lowercase(is black)
            if(board[row-1][column-1].islower()):
                # Sets location as a possible take square
                possible_moves[row-1][column-1] = 't'
        # Checks if possible to move right
        if(column<7):
            # Checks if location is lowercase(is black)
            if(board[row-1][column+1].islower()):
                # Sets location as a possible take square
                possible_moves[row-1][column+1] = 't'
    
    # get the enpassant location while clearing unnecessary information
    enpos = position[4].strip()[1:2]
    # check if there is possible enpassant
    if(enpos!='-'):
        # get the row and colomn of the enpassant square
        encol = int(ord(enpos[0])-97)
        enrow = -int(enpos[1])
        # Check if the enpassant is a possible move
        if(enrow==(row-1) and ((encol==(column-1)) or (encol==(column+1)))):
            # set the location as a possible enpassant square
            possible_moves[enrow][encol] = 'e'

    # Convert the list of lists(possible_moves) into a more readable format
    for x in range(len(possible_moves)):
        possible_moves[x] = ''.join(possible_moves[x])
    possible_moves = ','.join(possible_moves)
    return possible_moves