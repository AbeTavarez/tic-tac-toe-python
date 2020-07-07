# Python Tic-Tac-Toe...

# Create keys for the tic-tac-toe dictionary data stucture.
# There are 9 spaces in a TTTboard, just like in this hash # symbol.
SPACES = list("123456789")
# Our Constants for the string values.
X, O, EMPTY = "X", "O", " "

# Main fuction declaration.


def main():
    """Runs game of Tic Tac Toe"""
    print(":::::::::::::::::::::::::::::::::::::::")
    print(":::::::::Welcome to Tic-Tac-Toe::::::::")
    print("::::::::::::::::Python:::::::::::::::::")
    # Create Game Board
    gameboard = getBlankBoard()
    # X goes first, O goes next
    current_player, next_player = X, O

    while True:
        print(getBoardStr(gameboard))  # Display board on screen

        move = None
        while not isValidSpace(gameboard, move):
            print(f"Whats you move {current_player} ? (1-9)")
            move = input()
        updateBoard(gameboard, move, current_player)  # makes the move

        # checks if game is over
        if isWinner(gameboard, current_player):
            print(getBoardStr(gameboard))
            print(current_player + " has won the game!")
            break
        elif isBoardFull(gameboard):
            print(getBoardStr(gameboard))
            print("Is a tie!")
            break
        current_player, next_player = next_player, current_player  # swaps turns
        print("Thanks for playing!")

# Print Blank Tic-Tac-Toe Board to the screen


def getBlankBoard():
    """Create a new, blank tic-tac-toe board"""
    board = {}  # dictionary structure
    for space in SPACES:
        # setting the board keys as intigers and initiating spaces as empty spaces first.
        board[space] = EMPTY
    return board


def getBoardStr(board):
    """Return a text-representation of the board."""
    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9 '''.format(board['1'], board['2'], board['3'], board['4'], board['5'], board['6'], board['7'], board['8'], board['9'])


def isValidSpace(board, space):
    """Returns True if the space on the board is a valid space number
     and the space is blank. """
    return space in SPACES and board[space] == EMPTY


def isWinner(board, player):
    """Return true if player is a winner on this TTTBoard."""
    b, p = board, player  # Shorter names as "syntactic sugar".
    # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
    return ((b['1'] == b['2'] == b['3'] == p) or  # Across the top
            (b['4'] == b['5'] == b['6'] == p) or  # Across the middle
            (b['7'] == b['8'] == b['9'] == p) or  # Across the bottom
            (b['1'] == b['4'] == b['7'] == p) or  # Down the left
            (b['2'] == b['5'] == b['8'] == p) or  # Down the middle
            (b['3'] == b['6'] == b['9'] == p) or  # Down the right
            (b['3'] == b['5'] == b['7'] == p) or  # Diagonal
            (b['1'] == b['5'] == b['9'] == p))  # Diagonal


def isBoardFull(board):
    """Return True if every space on the board has been taken"""
    for space in SPACES:
        if board[space] == EMPTY:
            return False  # If a single space is blank, return False.
    return True  # No spaces are blank, so return True.


def updateBoard(board, space, mark):
    """Sets the space on the board to mark"""
    board[space] = mark


if __name__ == "__main__":
    main()  # Call main() if this module is run, but not when imported.
