from turtle import pos


def printBoard(board):
    ke = ""

    for i in range(1, (n * n) + 1):
        if i % n == 0:
            ke += ('|_' + board[i] + '_|' + '\n')
        else:
            ke += ('|_' + board[i] + '_')

    print(ke)


def clearBoard(board):
    for i, sym in enumerate(board):
        if board[i] == 'X' or board[i] == 'O':
            board[i] = ' '


def spotIsAvailable(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertSymbol(symbol, position):
    if spotIsAvailable(position):
        board[position] = symbol
        if(isTie()):
            printBoard(board)
            print("Tie")
            return -1
        if isWinner('X') and AI == 'X':
            printBoard(board)
            print('AI wins')
            return -1
        elif isWinner('O') and AI == 'O':
            printBoard(board)
            print('AI wins')
            return -1
        if isWinner('X') and human == 'X':
            printBoard(board)
            print('Human wins')
            return -1
        elif isWinner('O') and human == 'O':
            printBoard(board)
            print('Human wins')
            return -1
        return 0

    else:
        print('It is occupied!')
        position = int(input("Enter valid position: "))
        insertSymbol(symbol, position)
        return


def boardIsFilled(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def isTie():
    if boardIsFilled(board) and isWinner(AI) == False and isWinner(human) == False:
        return True
    else:
        return False

# def isWinner():
#     pass


def isWinner(symbol):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == symbol):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == symbol):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == symbol):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == symbol):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == symbol):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == symbol):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == symbol):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == symbol):
        return True
    else:
        return False


def compMove():
    bestScore = -1000
    bestMove = 0
    for key in possibleMoves:
        if (board[key] == ' '):
            board[key] = AI
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    if insertSymbol(AI, bestMove) == -1:
        main()
    printBoard(board)


def humanMove():
    position = int(input('Give field: '))
    if insertSymbol(human, position) == -1:
        main()
    printBoard(board)
    return


def minimax(board, depth, isMaximizing):
    if isWinner(AI):
        return 100
    elif isWinner(human):
        return -100
    elif isTie():
        return 0
    if isMaximizing:
        bestScore = -1000
        for key in possibleMoves:
            if (board[key] == ' '):
                board[key] = AI
                score = minimax(board, 0, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore
    else:
        bestScore = 800
        for key in possibleMoves:
            if (board[key] == ' '):
                board[key] = human
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


def main():
    print('Welcome to TIC TAC TOE, Mere Mortal!')
    clearBoard(board)
    printBoard(board)

    if human == 'X':
        print("OK! you will play as X! Don't regret afterwards")
    else:
        print("OK! you will play as O! Don't regret afterwards")

    while not isWinner(human) or isWinner(AI):
        if human == 'X':
            humanMove()
            compMove()
        else:
            compMove()
            humanMove()


while input('Do u wanna play y/n? ') == 'y':
    n = input('Size? ')
    n = int(n)

    board = [' ' for x in range((n * n) + 1)]
    possibleMoves = [x for x, symbol in enumerate(board)]
    if input('Fixed or Random turns (fixed/random)? ') == 'random':
        import random
        human = random.randint(1, 2)
        if human == 1:
            human = 'X'
            AI = 'O'
        else:
            human = 'O'
            AI = 'X'
    else:
        if input('Do u wan X or O?') == 'X':
            human = 'X'
            AI = 'O'
        else:
            human = 'O'
            AI = 'X'
    main()
