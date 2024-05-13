from urllib.parse import unquote_plus
from flask import Blueprint
from Move_Checks.Possible_moves import Possible_moves
import SQLcomm

Functions = Blueprint(__name__, 'Functions')

# initalize's the board and sets the position of the board to the default starting position
@Functions.route("/initalize_board")
def initalize_board():
    SQLcomm.initalize_board()
    return SQLcomm.get_board()

# clears the board and sets the position of the board to the default position
@Functions.route("/new_board")
def new_board():
    SQLcomm.clear_board()
    SQLcomm.initalize_board()
    return SQLcomm.get_board()
    
# sends the current position to the request
@Functions.route("/send_board")
def send_board():
    return SQLcomm.get_board()

# adds a move to the current game
@Functions.route("/add_move/<path:move>")
def add_move(move):
    move=unquote_plus(move)
    SQLcomm.add_move(str(move))
    return SQLcomm.get_board()

# clears the entire table storing the current position
@Functions.route("/clear_board")
def clear_board():
    SQLcomm.clear_board()
    return 'Board cleared'

# checks for posible moves of the piece that is at the current location
@Functions.route("/Check_moves/<path:location>")
def Check_moves(location):
    return Possible_moves(SQLcomm.get_board(),location)

# resets the board and sets the new position to the position provided
@Functions.route("/Set_Position/<path:position>")
def Set_Position(position):
    position=unquote_plus(position)
    SQLcomm.setBoard(str(position))
    return SQLcomm.get_board()