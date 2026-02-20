"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = sum(row.count(X) for  row in board)
    o = sum(row.count(O) for row in board)
    return X if x<=o else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if i < 0 or i >= 3 or j < 0 or j >= 3:
        raise Exception("Invalid action")
    if board[i][j] != EMPTY:
        raise Exception("Invalid action")
    new_board = [row.copy() for row in board]
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Rows
    lines = []
    for i in range(3):
        lines.append([board[i][j] for j in range(3)])

    # Columns
    for j in range(3):
        lines.append([board[i][j] for i in range(3)])

    # Diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for block in lines:
        if all(cell == X for cell in block):
            return X
        if all(cell == O for cell in block):
            return O

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else :
            return 0
    else :
        return 0

def min_value(board):
    if terminal(board) :
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def max_value(board):
    if terminal(board) :
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) :
        return None
    current = player(board)

    if current == X:
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
            elif value == 1 :
                return action
        return best_action
    else :
        best_value = math.inf
        best_action = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
            elif value == -1 :
                return action
        return best_action