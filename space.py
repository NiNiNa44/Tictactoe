import math
import copy

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
    count_X = 0
    count_O = 0

    for i in board:
        if i == X:
            count_X += 1
        if i == O:
            count_O += 1

    if count_X == count_O:
        return X
    else:
        return O


def actions(board):
    """
        Returns set of all possible actions (i, j) available on the board.
    """

    action = set()

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                action.add((i, j))

    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """



    # player's turn
    if board[action[0]][action[1]] != EMPTY:
        return Exception("action not valid")


    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    #Returns the winner of the game, if there is one.
    """
    win = EMPTY

    for i in range(3):
        # check for row
        if board[i][0] != EMPTY:
            win = board[i][0]
            if win == board[i][1] and win == board[i][2]:
                return win

        # check for column
    for i in range(3):
        if board[0][i] != EMPTY:
            win = board[0][i]
            if win == board[1][i] and win == board[2][i]:
                return win

    # check diagonally
    if board[0][0] != EMPTY:
        win = board[0][0]
        if win == board[1][1] and win == board[2][2]:
            return win
    if board[0][2] != EMPTY:
        win = board[0][2]
        if win == board[1][1] and win == board[2][0]:
            return win

    return None


def terminal(board):
    """
        Returns True if game is over, False otherwise.
    """

    if winner(board) == X or winner(board) == O:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """

    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        v = -float('inf')
        best_action = None

        for action in actions(board):
            current = max_x(result(board, action))
            if current > v:
                v = current
                best_action = action
        return best_action

    if player(board) == O:
        v = float('inf')
        best_action = None

        for action in actions(board):
            current = min_x(result(board, action))
            if current < v:
                v = current
                best_action = action
        return best_action


def max_x(board):
    if terminal(board):
        return utility(board)
    v = -math.inf

    for action in actions(board):
        v = max(v, min_x(board))
    return v


def min_x(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_x(board))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    Max = float("-inf")
    Min = float("inf")

    if player(board) == X:
        return Max_Value(board, Max, Min)[1]
    else:
        return Min_Value(board, Max, Min)[1]


def Max_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('-inf')
    for action in actions(board):
        test = Min_Value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];


def Min_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('inf')
    for action in actions(board):
        test = Max_Value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];

def minimax(board):
    """

    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        v = -float('inf')
        best_action = None

        for action in actions(board):
            current = max_x(result(board, action))
            if current > v:
                v = current
                best_action = action
        return best_action

    if player(board) == O:
        v = float('inf')
        best_action = None

        for action in actions(board):
            current = min_x(result(board, action))
            if current < v:
                v = current
                best_action = action
        return best_action


def max_x(board):
    if terminal(board):
        return utility(board)
    v = -math.inf

    for action in actions(board):
        v = max(v, min_x(result(board, action)))
    return v


def min_x(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_x(result(board, action)))
    return v
