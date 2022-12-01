def chunks(b, n):
    return [b[i:i+n] for i in range(1, len(b) - 1, n)]


def print_board(board):
    stringa = ""
    for i in range(1, len(board)):
        if i % (len(board) - 1) ** 0.5 == 0 and i != 0:
            stringa += "| " + board[i] + " |" + "\n"
        else:
            stringa += "| " + board[i] + " "
    print(stringa)


def transpose(board):
    return [[board[i][j] for i in range(len(board))] for j in range(len(board[0]))]


# board = ['_' for _ in range(26)]
board = ['_', '2', '1', '3', '4', '5', '6', '7', '8', '9']
# board = [i for i in enumerate(board)]
# board.remove(0)
print_board(board)

n = int((len(board) - 1) ** 0.5)
board = chunks(board, n)
print(board)
board = transpose(board)
print(board)
