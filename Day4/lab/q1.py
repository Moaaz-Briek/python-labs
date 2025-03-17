import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]

    def display(self):
        clear_console()
        print('----' * self.size + '-')
        for row in self.board:
            print('|', ' | '.join(row), '|')
            print('----' * self.size + '-')

    def update(self, row, col, symbol):
        if self.board[row][col] == ' ':
            self.board[row][col] = symbol
            return True
        return False

    def check_winner(self):
        # Check rows and columns
        for i in range(self.size):
            if all(self.board[i][j] == self.board[i][0] != ' ' for j in range(self.size)):
                return self.board[i][0]
            if all(self.board[j][i] == self.board[0][i] != ' ' for j in range(self.size)):
                return self.board[0][i]

        # Check diagonals
        if all(self.board[i][i] == self.board[0][0] != ' ' for i in range(self.size)):
            return self.board[0][0]
        if all(self.board[i][self.size - 1 - i] == self.board[0][self.size - 1] != ' ' for i in range(self.size)):
            return self.board[0][self.size - 1]

        return None

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                row, col = map(int, input(f'Player {self.symbol}, enter your move (row col): ').split())
                if 0 <= row < board.size and 0 <= col < board.size and board.update(row, col, self.symbol):
                    break
                print('Invalid move. Try again.')
            except ValueError:
                print('Invalid input. Please enter two integers for row and column.')

class Game:
    def __init__(self, size):
        self.board = Board(size)
        self.players = [Player('X'), Player('O')]
        self.current_player = 0

    def play(self):
        while True:
            self.board.display()
            self.players[self.current_player].make_move(self.board)

            winner = self.board.check_winner()
            if winner:
                self.board.display()
                print(f'Player {winner} wins!')
                break

            if self.board.is_full():
                self.board.display()
                print('It\'s a draw!')
                break

            self.current_player = 1 - self.current_player

# Main program
if __name__ == "__main__":
    print("Select board size:")
    print("1. 3x3")
    print("2. 4x4")
    print("3. 5x5")
    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice == 1:
        size = 3
    elif choice == 2:
        size = 4
    elif choice == 3:
        size = 5
    else:
        print("Invalid choice. Defaulting to 3x3.")
        size = 3

    game = Game(size)
    game.play()
