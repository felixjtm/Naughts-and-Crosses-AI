import copy
import Board


def start_game():
    board = Board.Board()
    print(next_symbol('X'))
    print("This is naughts & crosses AI")

    choice = 'N'
    while choice != 'X' and choice != 'O':
        print("Please enter whether you would like to play as X or O:", end=" ")
        choice = input().upper()

    play_game(board, choice)


def play_game(board, player_symbol):
    turn = 0
    ai_symbol = 'N'
    player_first = True
    if player_symbol == 'X':
        ai_symbol = 'O'
    elif player_symbol == 'O':
        player_first = False
        ai_symbol = 'X'
    else:
        print("ERROR: Player symbol invalid")

    result = board.check_if_end()
    while result == 'F':
        turn += 1
        print("Turn", turn)

        if player_first:
            player_turn(board, player_symbol)
            player_first = False
        else:
            ai_turn(board, ai_symbol)
            player_first = True

        result = board.check_if_end()

    if result == 'T':
        print("The game was a tie.")
    else:
        print(result, "wins!")


def player_turn(board, symbol):
    board.print_board()
    choice_is_valid = False
    while not choice_is_valid:
        choice = input("Select available location 1-9: ")
        if valid_choice(choice, board):
            choice_is_valid = True
            choice = int(choice)
            board.fill_square(choice, symbol)
            board.print_board()
        else:
            print("Please enter a valid character in a available location")


global count


def ai_turn(board, symbol):
    global count
    count = 0
    value = float('-inf')
    a = float('-inf')
    b = float('inf')
    best_move = 0
    for i in range(1, 10):
        if board.get_square(i) != 'X' and board.get_square(i) != 'O':
            board.fill_square(i, symbol)
            new_val = minimax(board, 10, False, symbol, a, b)
            board.undo_move()
            if new_val > value:
                value = new_val
                best_move = i

    print("Evaluated", count, "branches. Making move at square", best_move)
    board.fill_square(best_move, symbol)


def minimax(board, depth, is_max, symbol, a, b):
    global count
    count += 1
    result = board.check_if_end()
    if depth == 0 or result != 'F':
        if result == symbol:
            return 10 + depth
        elif result == 'T':
            return 0 + depth
        else:
            return -10 + depth
    if is_max:
        value = float('-inf')
        for i in range(1, 10):
            if board.get_square(i) != 'X' and board.get_square(i) != 'O':
                board.fill_square(i, symbol)
                value = max(value, minimax(board, depth - 1, False, symbol, a, b))
                board.undo_move()
                a = max(a, value)
                if a >= b:
                    break

        return value
    else:
        value = float('inf')
        for i in range(1, 10):
            if board.get_square(i) != 'X' and board.get_square(i) != 'O':
                board.fill_square(i, next_symbol(symbol))
                value = min(value, minimax(board, depth - 1, True, symbol, a, b))
                board.undo_move()
                b = min(b, value)
                if b <= a:
                    break

        return value


def next_symbol(symbol):
    if symbol == 'X':
        return 'O'
    else:
        return 'X'


def valid_choice(x, board):
    if x.isdigit():
        x = int(x)
        if 1 <= x <= 9:
            square = board.get_square(x)
            if square != 'X' and square != 'O':
                return True

    return False


start_game()
