from turtle import pos
import Move_Checks.Piece_logic.Black_rook as BlackRook
import Move_Checks.Piece_logic.White_rook as WhiteRook
import Move_Checks.Piece_logic.White_pawn as WhitePawn
import Move_Checks.Piece_logic.Black_pawn as BlackPawn
import Move_Checks.Piece_logic.Black_knight as BlackKnight
import Move_Checks.Piece_logic.White_knight as WhiteKnight
import Move_Checks.Piece_logic.White_king as WhiteKing
import Move_Checks.Piece_logic.Black_king as BlackKing
import Move_Checks.Piece_logic.Black_bishop as BlackBishop
import Move_Checks.Piece_logic.White_bishop as WhiteBishop
import Move_Checks.Piece_logic.Black_queen as BlackQueen
import Move_Checks.Piece_logic.White_queen as WhiteQueen
def Possible_moves(position,location):
    # Splits FEN position into a interable list
    position = position.split(',')

    # Gets the board from the position list, removes unnecessary characters, and splits the board by row
    board = position[1][2:-1].split('/')
    board = FenToBoard(board)# Translates the board from a FEN position into a more readable format
    row = board[int(location[0])]# locates the row using the position provided
    pieceType = row[int(location[1])] # locates the piece at the position provided

    # Check for possible moves
    # if it is black's turn to move
    if(position[2].strip()[1:-1]=='b'):
        # check which piece is currently selected
        match pieceType:
            # if black pawn selected
            case 'p':
                return BlackPawn.Black_pawn(position, board, location)
            # if black knight selected
            case 'n':
                return BlackKnight.Black_knight(position, board, location)
            # if black king selected
            case 'k':
                return BlackKing.Black_king(position, board, location)
            # if black bishop is selected
            case 'b':
                return BlackBishop.Black_bishop(position, board, location)
            # if black rook is selected
            case 'r':
                return BlackRook.Black_rook(position,board,location)
            # if black queen is selected
            case 'q':
                return BlackQueen.Black_queen(position, board, location)
    # if it is white's turn to move
    elif(position[2].strip()[1:-1]=='w'):
        # check which piece is currently selected
        match pieceType:
            # if white pawn selected
            case 'P':
                return WhitePawn.White_pawn(position, board, location)
            # if white knight selected
            case 'N':
                return WhiteKnight.White_knight(position, board, location)
            # if white king
            case 'K':
                return WhiteKing.White_king(position, board, location)
            # if white bishop is selected
            case 'B':
                return WhiteBishop.White_bishop(position, board, location)
            # if white rook is selected
            case 'R':
                return WhiteRook.White_rook(position, board, location)
            # if white queen is selected
            case 'Q':
                return WhiteQueen.White_queen(position, board, location)
    return board

def FenToBoard(board):
    # creates list of rows to be returned later
    newBoard=[]
    # interates through the current board/FEN position
    for row in board:
        # creates a string to store the translated row
        newrow = ''
        # iterates through the rows in the current board/FEN position
        for box in row:
            # if the current char is not a digit, just input the char as is
            if not box.isdigit():
                newrow+=box
            # if the current char is a digit, replace it with its respective number of periods
            else:
                newrow+='.'*int(box)
        # append the translated row to the new board
        newBoard.append(newrow)
    # return the fully translated board
    return newBoard