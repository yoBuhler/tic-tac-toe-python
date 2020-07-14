Move = {
    "row": 0,
    "col": 0
}

player = 'x'
opponent = 'o'


def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '_'):
                return True
    return False


def evaluate(b):
    for row in range(3):
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
            if (b[row][0] == player):
                return +10
            elif (b[row][0] == opponent):
                return -10

    for col in range(3):
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):
            if (b[0][col] == player):
                return +10
            elif (b[0][col] == opponent):
                return -10

    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):
        if (b[0][0] == player):
            return +10
        elif (b[0][0] == opponent):
            return -10

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):
        if (b[0][2] == player):
            return +10
        elif (b[0][2] == opponent):
            return -10
    return 0


def minimax(board, depth, isMax):
    score = evaluate(board)
    if (score == 10):
        return score

    if (score == -10):
        return score

    if (isMovesLeft(board) == False):
        return 0

    if (isMax):
        best = -1000

        for i in range(3):
            for j in range(3):
                if (board[i][j] == '_'):
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'

        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if (board[i][j] == '_'):
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best


def findBestMove(board):
    bestVal = -1000
    bestMove = Move
    bestMove["row"] = -1
    bestMove["col"] = -1

    for i in range(3):
        for j in range(3):
            if (board[i][j] == '_'):
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'
                if (moveVal > bestVal):
                    bestMove["row"] = i
                    bestMove["col"] = j
                    bestVal = moveVal

    return bestMove

def printTable(board):
    print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])


import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def start():
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    while (True):
        row = int(input("Digite uma linha (0-2): "))
        while (row < 0 or row > 2):
            row = int(input("Digite uma linha (0-2): "))
        col = int(input("Digite uma coluna (0-2): "))
        while (col < 0 or col > 2):
            col = int(input("Digite uma coluna (0-2): "))
        
        if board[row][col] != '_':
            print('Movimento errado linha: {}, coluna: {}, valor: {}'.format(row, col, board[row][col]))
        else:
            board[row][col] = player
            if evaluate(board) > 0:
                printTable(board)
                input("{} Venceu".format(player))
                break
            if not isMovesLeft(board):
                printTable(board)
                input("Deu Velha")
                break
            positionCPU = findBestMove(board)
            board[positionCPU["row"]][positionCPU["col"]] = opponent
            if evaluate(board) < 0:
                printTable(board)
                input("{} Venceu".format(opponent))
                break
            if not isMovesLeft(board):
                printTable(board)
                input("Deu Velha")
                break
            printTable(board)

while True:
    cls()
    print("Menu")
    print("1 - Jogar")
    print("2 - Sair")
    option = int(input())
    if option == 1:
        print("Selecione seu marcador")
        print("1 - X")
        print("2 - O")
        tag = int(input())
        while(tag != 1 and tag != 2):
            tag = int(input("Tente novamente: "))
        if tag == 1:
            player = 'X'
            opponent = 'O'
        else:
            player = 'O'
            opponent = 'X'
        start()
    elif option == 2:
        print("Bye")
        exit()