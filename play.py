import random
from itertools import product
from copy import deepcopy
from collections import Counter
from random import choice


def get_legal_moves(board):
    """
    >>> get_legal_moves([['X','X','X'],['X',' ','X'],['X','X','X']])
    [(1, 1)]

    >>> len(get_legal_moves([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]))
    9

    >>> get_legal_moves([['X','X','X'],['X','X','X'],['X','X','X']])
    []
    """

    return [(x, y) for x, y in product(range(3), range(3)) if board[y][x] == " "]


def my_agent(board):
    """
    Implement your agent here. It is expected that you will perform a search over a game tree.

    It has access to the board as a 3x3 array. Players are denoted as

    - X - You have played here
    - O - Your opponent has played here
    - ' ' (Space) - No one has played here

    You must return a valid space to play as a 2d tuple. Examples:

    - (1,1) - Center of the board
    - (0,2) - Bottom left of the board
    - (2,0) - Top right of the board

    The random_agent and ordered_agent may also show helpful examples.
    """

    return random_agent(board)


def random_agent(board):
    """
    Random Agent

    Very basic agent that simply selects a random legal move
    """

    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)

        if board[y][x] == " ":
            return (x, y)


def ordered_agent(board):
    """
    Ordered Agent

    Simple agent that selects legal moves in order from left to right and top
    to bottom after playing the center.
    """

    if board[1][1] == " ":
        return (1, 1)

    for x in range(3):
        for y in range(3):
            if board[y][x] == " ":
                return (x, y)


def show(board):
    """
    Displays the board
    """

    print("+---+")
    for y in range(0, 3):
        print(f"|{''.join(board[y])}|")
    print("+---+")


def get_winner(board):
    """
    Returns the winner for a board state

    >>> get_winner([['X','X','X'],['O','O','X'],['X','O','O']])
    'X'

    >>> get_winner([['O','X','X'],['X','O','X'],['X','O','O']])
    'O'

    >>> get_winner([['O','X','X'],['X','X','O'],['X','O','O']])
    'X'

    >>> get_winner([['X','O','X'],['X','O','X'],['O','X','O']])
    'No one'

    >>> get_winner([['O','O','X'],['X','X','O'],['O','X','X']])
    'No one'
    """

    rows = []

    for x in range(3):
        rows.append({board[0][x], board[1][x], board[2][x]})

    for y in range(3):
        rows.append({board[y][0], board[y][1], board[y][2]})

    rows.append({board[0][0], board[1][1], board[2][2]})
    rows.append({board[2][0], board[1][1], board[0][2]})

    for row in rows:
        if len(row) == 1 and row != {" "}:
            return row.pop()

    if not "' '" in str(board):
        return "No one"


def play(agents, quiet=True):
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]

    for i in range(9):
        move = agents[i % 2](board.copy())

        if board[move[1]][move[0]] == " ":
            board[move[1]][move[0]] = "XO"[i % 2]

            if not quiet:
                show(board)
        else:
            raise ValueError("Illegal move")

        if get_winner(board):
            if not quiet:
                print(f"{get_winner(board)} wins!")
            return get_winner(board)
            break


def get_win_rate(agents, runs=1000):
    counter = Counter()

    for i in range(runs):
        counter.update(play(agents))

    return counter["X"] / (counter["X"] + counter["O"])


if __name__ == "__main__":
    player = my_agent
    opponent = random_agent

    play([player, opponent], quiet=False)
    print(f"Win rate: {get_win_rate([player, opponent])}")
