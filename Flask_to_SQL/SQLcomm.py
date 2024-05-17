import mysql.connector

def initalize_board():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password",
        database="chess"
    )
    cursor = conn.cursor()
    # Creates the table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS board (
            move_num INT AUTO_INCREMENT PRIMARY KEY,
            board VARCHAR(255),
            to_move VARCHAR(1),
            castle VARCHAR(4),
            enpassant VARCHAR(2),
            halfmoves INT ,
            fullmoves INT
        )
    ''')
    # alters the board to auto increment
    cursor.execute("ALTER TABLE board AUTO_INCREMENT=1")
    # Inputs the base position into the board
    cursor.execute('''
        INSERT INTO board (board,to_move,castle,enpassant,halfmoves,fullmoves) VALUES (%s,%s,%s,%s,%s,%s)
    ''', (('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR','w','KQkq','-',0,1)))
    # Commit changes and close the connection
    conn.commit()
    conn.close()

def get_board():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password",
        database="chess"
    )
    cursor = conn.cursor()
    # gets the curent board and returns it
    cursor.execute('''
        SELECT * FROM BOARD ORDER BY move_num DESC
    ''')
    row = str(cursor.fetchone())
    conn.close
    return row

def clear_board():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password",
        database="chess"
    )
    cursor = conn.cursor()
    # delets the entire table
    cursor.execute('''
        DELETE FROM board
    ''')
    conn.commit()
    conn.close

def add_move(move):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password",
        database="chess"
    )
    cursor = conn.cursor()
    # splits the input into its respective parts
    move=move.split(' ')
    board=move[0]
    to_move=move[1]
    castle=move[2]
    enpassant=move[3]
    halfmoves=int(move[4])
    fullmoves=int(move[5])

    # using those parts it inputs it into its respective columbs
    cursor.execute('''
        INSERT INTO board (board,to_move,castle,enpassant,halfmoves,fullmoves) VALUES (%s,%s,%s,%s,%s,%s)
    ''', ((board,to_move,castle,enpassant,halfmoves,fullmoves)))

    conn.commit()
    conn.close()

def setBoard(position):
    clear_board()

    position = position.split(' ')
    position[-1] = int(float(position[-1]))
    position[-2] = int(float(position[-2]))
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password",
        database="chess"
    )
    cursor = conn.cursor()
    # Creates the board and its sections
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS board (
            move_num INT AUTO_INCREMENT PRIMARY KEY,
            board VARCHAR(255),
            to_move VARCHAR(1),
            castle VARCHAR(4),
            enpassant VARCHAR(2),
            halfmoves INT ,
            fullmoves INT
        )
    ''')
    # alters the board so that it auto increments
    cursor.execute("ALTER TABLE board AUTO_INCREMENT=1")
    # Insert the inputted position into the board
    cursor.execute('''
        INSERT INTO board (board,to_move,castle,enpassant,halfmoves,fullmoves) VALUES (%s,%s,%s,%s,%s,%s)
    ''', (position))
    # Commit changes and close the connection
    conn.commit()
    conn.close()