import random
from collections import Counter

def agent1(board):
    while True:
        x = random.randint(0,2)
        y = random.randint(0,2)

        if board[y][x] == ' ':
            return (x,y)

def agent2(board):
    if board[1][1] == ' ':
        return (1,1)

    for x in range(3):
        for y in range(3):
            if board[y][x] == ' ':
                return (x,y)

def show(board):
    print("+---+")
    for y in range(0,3):
        print(f"|{''.join(board[y])}|")
    print("+---+")

def get_winner(board):
    rows = []

    for x in range(3):
        rows.append({board[0][x], board[1][x], board[2][x]})

    for y in range(3):
        rows.append({board[y][0], board[y][1], board[y][2]})

    rows.append({board[0][0], board[1][1], board[2][2]})
    rows.append({board[2][0], board[1][1], board[0][2]})

    for row in rows:
        if len(row) == 1 and row != {' '}:
            return row.pop()

def play(agents,quiet=True):
    board = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' '],
    ]

    for i in range(9):
        move = agents[i%2](board)

        if board[move[1]][move[0]] == ' ':                        
            board[move[1]][move[0]] = 'XO'[i%2]
            
            if not quiet:
                show(board)
        else:
            raise ValueError("Illegal move")
        

        if get_winner(board):
            if not quiet:
                print(f"{get_winner(board)} wins!")
            return get_winner(board)
            break
    else:
        if not quiet:
            print("Tie!")
        return 'T'

def get_win_rate(agents, runs=10000):
    counter = Counter()

    for i in range(runs):
        counter.update(play(agents))

    return counter['X'] / (counter['X'] + counter['O'])

if __name__ == '__main__':
    play([agent1, agent2], quiet=False)
    print(f"Win rate for agent1: {get_win_rate([agent1, agent2])}")
