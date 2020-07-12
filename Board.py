import numpy as np


class Board:

    def __init__(self):
        self.board = np.array([['1', '2', '3'],
                               ['4', '5', '6'],
                               ['7', '8', '9']])

        # 2d array which stores the different combinations of locations which, if are the same, mean they have won
        # 0 1 2
        # 3 4 5
        # 6 7 8
        self.winConditions = np.array([[0, 1, 2],
                                       [0, 3, 6],
                                       [0, 4, 8],
                                       [6, 7, 8],
                                       [2, 5, 8],
                                       [3, 4, 5],
                                       [1, 4, 7],
                                       [6, 4, 2]])

        # Stores the previous move made on the board
        self.prev_move = []

    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=" ")
            print("")

    def get_board(self):
        return self.board

    def check_if_end(self):
        for condition in self.winConditions:
            y = condition // 3
            x = condition % 3

            if self.board[y[0]][x[0]] == self.board[y[1]][x[1]] and self.board[y[0]][x[0]] == self.board[y[2]][x[2]]:
                return self.board[y[0]][x[0]]  # Returns the symbol which has won

        for line in self.board:
            for square in line:
                if square != 'X' and square != 'O':
                    return 'F'  # The board is not full

        return 'T'  # The board is full

    def undo_move(self):
        #print(self.prev_move)
        move = self.prev_move.pop()
        self.board[(move - 1) // 3][(move - 1) % 3] = chr(move+48)
        #self.print_board()

    def fill_square(self, choice, symbol):
        self.board[(choice - 1) // 3][(choice - 1) % 3] = symbol
        self.prev_move.append(choice)

    # Takes a number 1-9, converts to the appropriate location within the board and returns that square
    def get_square(self, choice):
        return self.board[(choice - 1) // 3][(choice - 1) % 3]

    def get_prev_move(self):
        return self.prev_move
