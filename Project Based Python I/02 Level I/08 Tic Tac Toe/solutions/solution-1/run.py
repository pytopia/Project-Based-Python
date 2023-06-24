# Source Code Link:
# https://hackr.io/blog/python-projects

import random

class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        
        self.board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-'],
        ]

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def has_player_won(self, player):
        n = len(self.board)
        board_values = set()

        # check rows
        for i in range(n):
            for j in range(n):
                board_values.add(self.board[i][j])

            if board_values == {player}:
                return True
            else:
                board_values.clear()

        # check cols
        for i in range(n):
            for j in range(n):
                board_values.add(self.board[j][i])

            if board_values == {player}:
                return True
            else:
                board_values.clear()

        # check diagonals
        for i in range(n):
            board_values.add(self.board[i][i])
        if board_values == {player}:
            return True
        else:
            board_values.clear()
        
        board_values.add(self.board[0][2])
        board_values.add(self.board[1][1])
        board_values.add(self.board[2][0])
        if board_values == {player}:
            return True
        else:
            return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()

    def start(self):
        self.create_board()
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            try:
                self.show_board()
                print(f'\nPlayer {player} turn')

                row, col = list(
                    map(int, input(
                        'Enter row & column numbers to fix spot: ').split()))
                print()

                if col is None:
                    raise ValueError(
                        'not enough values to unpack (expected 2, got 1)')

                self.fix_spot(row - 1, col - 1, player)

                game_over = self.has_player_won(player)
                if game_over:
                    print(f'Player {player} wins the game!')
                    continue

                game_over = self.is_board_filled()
                if game_over:
                    print('Match Draw!')
                    continue

                player = self.swap_player_turn(player)

            except ValueError as err:
                print(err)

        print()
        self.show_board()


if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()