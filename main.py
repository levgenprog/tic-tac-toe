import math
from random import choice, randint
import time


def is_winner(board, symbol):
    def chunks(b, n):
        return [b[i:i+n] for i in range(1, len(b) - 1, n)]
    n = int((len(board) - 1) ** 0.5)
    board = chunks(board, n)

    def checkRows(board):
        for row in board:
            if len(set(row)) == 1:
                return row[0]
        return 0

    def checkDiagonals(board):
        if len(set([board[i][i] for i in range(len(board))])) == 1:
            return board[0][0]
        if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
            return board[0][len(board)-1]
        return 0

    def transpose(board):
        return [[board[i][j] for i in range(len(board))] for j in range(len(board[0]))]

    def checkWin(board):
        # transposition to check rows, then columns
        for newBoard in [board, transpose(board)]:
            result = checkRows(newBoard)
            if result:
                return result
        return checkDiagonals(board)
    if checkWin(board) == symbol:
        return True
    else:
        return False

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


def is_draw(board):
    if is_board_filled(board) and not is_winner(board, "X") and not is_winner(board, "O"):
        return True
    else:
        return False


def play_again():
    again = input("Wanna play again?[y/n] ").upper()
    if again == "Y":
        main()
    else:
        print("Buy")
        exit()


def is_free(board, position):
    return True if board[position] == '_' else False


def is_board_filled(board):
    return False if board.count('_') > 1 else True


def available_moves(board):
    lst = [i for i, s in enumerate(board) if s == "_"]
    lst.remove(0)
    return lst


def make_move(board, symbol, position):
    if is_free(board, position):
        board[position] = symbol
        print_board(board)
        if(is_draw(board)):
            print("Draw")
            play_again()
        elif is_winner(board, "X") and symbol == "X":
            print('X win')
            play_again()
        elif is_winner(board, "O") and symbol == "O":
            print('O wins')
            play_again()


def player_move(player, board):
    while True:
        try:
            position = int(input("Enter the cell: "))
            if position < 1 or position > len(board) - 1:
                raise ValueError
        except (KeyError, ValueError):
            print(
                f'You should inter an integer between 1 and {len(board) - 1}')
        if not is_free(board, position):
            print(("{0} is occupied").format(position))
        else:
            break
    make_move(board, player, position)


def can_win(board, player):
    for key in available_moves(board):
        board[key] = player
        if is_winner(board, player):
            board[key] = "_"
            return key
        board[key] = "_"
    return 0


def even_move(board):
    for key in available_moves(board):
        if key % 2 == 0:
            return key
    return 0


def comp_move_brute(ai, board, cnt):
    hum = "X" if ai == "O" else "O"
    time.sleep(1)
    if cnt == 0:  # x
        move = 1
    elif cnt == 1:  # o
        if 5 in available_moves(board):
            move = 5
        else:
            move = 1
    elif cnt == 2:  # x
        if 9 in available_moves(board):
            move = 9
        else:
            move = 3
    elif cnt == 3:  # o
        prevent = can_win(board, hum)
        if prevent != 0:
            move = prevent
        else:
            move = even_move(board)
            if move == 0:
                move = choice(available_moves(board))
    elif cnt == 4:  # x
        win = can_win(board, ai)
        prevent = can_win(board, hum)
        if win != 0:
            move = win
        elif prevent != 0:
            move = prevent
        elif 7 in available_moves(board):
            move = 7
        else:
            move = 3
    elif cnt == 5:  # o1
        win = can_win(board, ai)
        prevent = can_win(board, hum)
        if win != 0:
            move = win
        elif prevent != 0:
            move = prevent
        else:
            move = even_move(board)
            if move == 0:
                move = choice(available_moves(board))
    else:  # x, o, x and game shold be over\
        win = can_win(board, ai)
        prevent = can_win(board, hum)
        if win != 0:
            move = win
        elif prevent != 0:
            move = prevent
        else:
            move = choice(available_moves(board))
    make_move(board, ai, move)


def comp_move_minimax(player, board, *args):
    time.sleep(1)
    if len(available_moves(board)) == len(board) - 1:
        move = randint(1, len(board) - 1)
    else:
        max = -math.inf
        for key in available_moves(board):
            board[key] = player
            if is_winner(board, player):
                move = key
                board[key] = "_"
                break
            score = minimax(board, player, False)
            board[key] = "_"
            if(score > max):
                max = score
                move = key
    make_move(board, player, move)


def minimax(board, ai, grows_up):
    hum = "X" if ai == "O" else "O"
    if is_winner(board, ai):
        return 1000
    elif is_winner(board, hum):
        return -1000
    elif is_draw(board):
        return 0
    if grows_up:
        max_eval = -math.inf
        for key in available_moves(board):
            board[key] = ai
            score = minimax(board, ai, False)
            board[key] = "_"
            max_eval = max(max_eval, score)
        return max_eval
    else:
        min_eval = math.inf
        for key in available_moves(board):
            board[key] = hum
            score = minimax(board, ai, True)
            board[key] = "_"
            min_eval = min(min_eval, score)
        return min_eval


def comp_move_minimax_alfa_beta(player, board, *args):
    time.sleep(1)
    if len(available_moves(board)) == len(board) - 1:
        move = randint(1, len(board) - 1)
    else:
        best = -math.inf
        alfa = -math.inf
        beta = math.inf
        for key in available_moves(board):
            board[key] = player
            if is_winner(board, player):
                move = key
                board[key] = "_"
                break
            score = minimax_alfa_beta(board, player, False, alfa, beta)
            board[key] = "_"
            if(score > best):
                best = score
                move = key
    make_move(board, player, move)


def minimax_alfa_beta(board, ai, grows_up, alfa, beta):
    hum = "X" if ai == "O" else "O"
    if is_winner(board, ai):
        return 1000
    elif is_winner(board, hum):
        return -1000
    elif is_draw(board):
        return 0
    if grows_up:
        max_eval = -math.inf
        for key in available_moves(board):
            board[key] = ai
            score = minimax_alfa_beta(board, ai, False, alfa, beta)
            board[key] = "_"
            max_eval = max(max_eval, score)
            alfa = max(alfa, score)
            if beta <= alfa:
                break
        return max_eval
    else:
        min_eval = math.inf
        for key in available_moves(board):
            board[key] = hum
            score = minimax_alfa_beta(board, ai, True, alfa, beta)
            board[key] = "_"
            min_eval = min(min_eval, score)
            beta = min(beta, score)
            if beta <= alfa:
                break
        return min_eval


def print_board(board):
    stringa = ""
    for i in range(1, len(board)):
        if i % (len(board) - 1) ** 0.5 == 0 and i != 0:
            stringa += "| " + board[i] + " |" + "\n"
        else:
            stringa += "| " + board[i] + " "
    print(stringa)


def main():
    ai_choice = ""
    player_choice = ""
    while True:
        try:
            difficulty = int(input("Choose difficulty:\nType 0 - for beatable, \n"
                                   "Type 1 - for minimax unbeatable, \n"
                                   "Type 2 - for super mega minimax alpha beta puring difficulty "))
            if difficulty > 2 or difficulty < 0:
                raise ValueError
            break
        except (KeyError, ValueError):
            print(f'Incorrect difficulty {difficulty}, try again')
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
    while ai_choice == "":
        try:
            player_choice = input(
                """Choose your character: type X or O.\nor type random if you do not give a shit """).upper()
            print()
            if player_choice == "RANDOM":
                rnd = randint(0, 1)
                if rnd == 0:
                    player_choice = "O"
                    ai_choice = "X"
                else:
                    player_choice = "X"
                    ai_choice = "O"
            elif player_choice == "X":
                ai_choice = "O"
            elif player_choice == "O":
                ai_choice = "X"
            else:
                raise ValueError
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print(f'There is no such a player {player_choice}, try again')

    print("Player " + player_choice)
    print("AI " + ai_choice)
    board = ['_' for _ in range(26)]
    match difficulty:
        case 0:
            comp_move = comp_move_brute
        case 1:
            comp_move = comp_move_minimax
        case 2:
            comp_move = comp_move_minimax_alfa_beta
    if player_choice == "X":
        print_board(board)
    try:
        cnt = 0
        while not is_winner(board, ai_choice) or not is_winner(board, player_choice) or not is_draw(board):
            if player_choice == "X":
                player_move(player_choice, board)
                cnt += 1
                comp_move(ai_choice, board, cnt)
                cnt += 1
            else:
                comp_move(ai_choice, board, cnt)
                cnt += 1
                player_move(player_choice, board)
                cnt += 1
    except (EOFError, KeyboardInterrupt):
        print('Bye')
        exit()


if __name__ == '__main__':
    main()
