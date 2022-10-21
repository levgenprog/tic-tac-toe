import math
from random import choice, randint
import time


def is_winner(board, symbol):
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
    again = input("Wanna play again?[y/n]").upper()
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
        if is_winner(board, "X") and symbol == "X":
            print('X win')
            play_again()
        elif is_winner(board, "O") and symbol == "O":
            print('O wins')
            play_again()
        else:
            return True
    return False


def player_move(player, board):
    while True:
        try:
            position = int(input("Enter the cell: "))
            if position < 1 or position > 9:
                raise ValueError
        except (KeyError, ValueError):
            print('You should inter an integer between 1 and 9')
        else:
            if not make_move(board, player, position):
                print(("{0} is occupied").format(position))
            else:
                break


def can_win(board, player):
    for key in available_moves(board):
        board[key] = player
        if is_winner(board, player):
            return key
    return 0


def even_move(board):
    for key in available_moves(board):
        if key % 2 == 0:
            return key
    return 0


def comp_move(ai, board, cnt):
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
            move = even_move(board, board)
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
    elif cnt == 5:  # o
        win = can_win(board, ai)
        prevent = can_win(board, hum)
        if win != 0:
            move = win
        elif prevent != 0:
            move = prevent
        else:
            move = even_move(board)
    else:  # x, o, x and game shold be over
        win = can_win(board, ai)
        prevent = can_win(board, hum)
        if win != 0:
            move = win
        elif prevent != 0:
            move = prevent
        else:
            move = choice(available_moves(board))
    make_move(board, ai, move)

    # if len(available_moves(board)) == 9:
    #     move = randint(1, 9)
    # else:
    #     max = -math.inf
    #     for key in available_moves(board):
    #         board[key] = player
    #         score = minimax(board, player, False)
    #         board[key] = "_"
    #         if(score > max):
    #             max = score
    #             move = key
    # make_move(board, player, move)


# def minimax(board, ai, grows_up):
#     hum = "X" if ai == "O" else "O"
#     if is_winner(board, ai):
#         return 100
#     elif is_winner(board, hum):
#         return -100
#     elif is_draw(board):
#         return 0
#     if grows_up:
#         max = -math.inf
#         for key in available_moves(board):
#             board[key] = ai
#             score = minimax(board, ai, False)
#             board[key] = "_"
#             if(score > max):
#                 max = score
#         return max
#     else:
#         max = math.inf
#         for key in available_moves(board):
#             board[key] = hum
#             score = minimax(board, ai, True)
#             board[key] = "_"
#             if(score < max):
#                 max = score
#         return max


def print_board(board):
    stringa = ""
    for i in range(1, len(board)):
        if i % 3 == 0 and i != 0:
            stringa += "| " + board[i] + " |" + "\n"
        else:
            stringa += "| " + board[i] + " "
    print(stringa)


def main():
    ai_choice = ""
    player_choice = ""
    while ai_choice == "":
        try:
            print(
                """Choose your character: type X or O.\nor type random if you do not give a shit """)
            player_choice = input().upper()
            print(player_choice)
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
                print('Try again falk')
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    print("Player " + player_choice)
    print("AI " + ai_choice)
    board = ['_' for _ in range(10)]
    if player_choice == "X":
        print_board(board)
    try:
        cnt = 0
        while not is_winner(board, ai_choice) or is_winner(board, player_choice) or is_draw(board):
            if player_choice == "X":
                player_move(player_choice, board)
                comp_move(ai_choice, board, cnt)
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
