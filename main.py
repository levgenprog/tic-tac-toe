from random import randint


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


def is_free(board, position):
    return True if board[position] == '_' else False


def is_board_filled(board):
    return False if board.count('_') > 1 else True


def available_moves(board):
    return [i for i, s in enumerate(board) if s == "_"]


def empty_cells(board):
    return "_" in board


def num_empty_cell(board):
    return board.count("_")


def make_move(board, symbol, position):
    if is_free(board, position):
        board[position] = symbol
        if(is_draw(board)):
            print("Tie")
            return -1
        if is_winner(board, "X") and symbol == "X":
            print('X win')
            return -1
        elif is_winner(board, "O") and symbol == "O":
            print('O wins')
            return -1
        return 0


def player_move(player, board):
    position = int(input("Enter the cell: "))
    if make_move(board, player, position) == -1:
        pass
    print_board(board)
    return


def comp_move(player, board):
    move = 0


def print_board(board):
    stringa = ""
    for i in range(1, len(board)):
        if i % 3 == 0 and i != 0:
            stringa += board[i] + "\n"
        else:
            stringa += board[i]
    print(stringa)


def main():
    ai_choice = ""
    player_choice = ""
    while ai_choice == "":
        try:
            player_choice = input(
                """Choose your character: type X or O.\n or typr random if you do not give a shit """).upper()
            if player_choice == "RANDOM":
                rnd = randint(0, 1)
                if rnd == 0:
                    player_choice = "O"
                else:
                    player_choice = "X"
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
    print_board(board)

    while not is_winner(board, ai_choice) or is_winner(board, player_move):
        if player_choice == "X":
            player_move(player_choice, board)


if __name__ == '__main__':
    main()
