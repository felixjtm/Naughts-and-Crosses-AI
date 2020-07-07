import Board


def start_game():
    board = Board.Board()
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


def ai_turn(board, symbol):
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


def valid_choice(x, board):
    if x.isdigit():
        x = int(x)
        if 1 <= x <= 9:
            square = board.get_square(x)
            if square != 'X' and square != 'O':
                return True

    return False


start_game()
