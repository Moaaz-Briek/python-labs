#1. Tic-Tac-Toe:
import os
def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')


class Board:
    def __init__(self):
        self.board = [['   ' for _ in range(3)] for _ in range(3)]

    def display(self):
        print('-------------')
        for row in self.board:
            print('|', '|'.join(row), '|', sep='')
            print('-------------')

    def update(self, row, col, symbol):
        if self.board[row][col] == '   ':
            self.board[row][col] = f' {symbol} '
            return True
        return False

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '   ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '   ':
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '   ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '   ':
            return self.board[0][2]

        return None

    def is_full(self):
        return all(self.board[i][j] != '   ' for i in range(3) for j in range(3))


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                row, col = map(int, input(f'Player {self.symbol}, enter your move (row col): ').split())
                if 0 <= row < 3 and 0 <= col < 3:
                    if board.update(row, col, self.symbol):
                        break
                    else:
                        print('That spot is already taken. Try again.')
                else:
                    print('Invalid move. Please enter row and column between 0 and 2.')
            except ValueError:
                print('Invalid input. Please enter two integers for row and column.')


class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.current_player = self.player1

    def play(self):
        clear_console()
        while True:
            self.board.display()

            self.current_player.make_move(self.board)
            clear_console()

            winner = self.board.check_winner()
            if winner:
                self.board.display()
                print(f'Player {winner} wins!')
                break

            if self.board.is_full():
                self.board.display()
                print('It is a draw!')
                break

            self.current_player = self.player2 if self.current_player == self.player1 else self.player1



""" game = Game()
game.play() """


#2. DataClass:
'''
A dataclass in Python (introduced in version 3.7) is a decorator that automatically generates special methods for classes used to store data.
These methods include __init__, __repr__, __eq__, and others, reducing code.
It simplifies class creation for data storage, reducing repetitive code.

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str = 'Unknown'

person = Person('Alice', 30)
print(person)  # Person(name='Alice', age=30, city='Unknown')
'''


#3. Summarize Multi Inheritance in Python:
'''
Multiple inheritance in Python enables a class to derive attributes and methods from multiple parent classes. The sequence in which these parent classes are searched for methods and attributes is governed by the Method Resolution Order (MRO). MRO is calculated using the C3 linearization algorithm, which ensures a logical and consistent order of class inheritance.

Key Points:
1. MRO defines the order in which base classes are traversed when accessing a method or attribute.
2. The C3 algorithm adheres to three principles:
   - Inheritance hierarchy: The order respects the structure of the inheritance graph.
   - Local priority: A class is checked before its superclasses.
   - Consistency: The order remains stable and predictable.
3. You can view the MRO of a class using the `__mro__` attribute or the `mro()` method.

Example:

class A:
    def method(self):
        print('A')

class B(A):
    def method(self):
        print('B')

class C(A):
    def method(self):
        print('C')

class D(B, C):
    pass

d = D()
print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

In this example:
- The MRO for class `D` is `D -> B -> C -> A -> object`.
- When `d.method()` is called, Python follows the MRO to locate the `method`, finding it first in class `B`.

Summary:
- Python's multiple inheritance relies on the C3 linearization algorithm to determine the MRO.
- MRO ensures a clear and predictable sequence for method and attribute resolution.
- Use `__mro__` or `mro()` to examine the inheritance order of a class.
'''

#4. Dictionary Comprehension Example:
'''
squares = {x**2: x**3 for x in range(1, 6)}
print(squares)      # output: {1: 1, 4: 8, 9: 27, 16: 64, 25: 125}
'''

#5. Composition:
'''
class Engine:
    def __init__(self, fuel_type, horsepower):
        self.fuel_type = fuel_type
        self.horsepower = horsepower

    def __str__(self):
        return f'{self.horsepower} HP {self.fuel_type} engine'


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def car_info(self):
        return f'{self.make} {self.model} with a {self.engine}'


engine1 = Engine('petrol', 150)
car1 = Car('Toyota', 'Camry', engine1)

print(car1.car_info())  # output: Toyota Camry with a 150 HP petrol engine
'''
#6. Vector Class
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y if isinstance(other,Vector) else Vector(self.x * other, self.y * other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return round((self.x**2 + self.y**2)**0.5)

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError('Index out of range for 2D vector')

'''
# Example usage:
v1 = Vector(2, 4)
v2 = Vector(3, 1)

print(v1)                   # output: Vector(2, 4)
print(v1 + v2)              # output: Vector(5, 5)
print(v1 - v2)              # output: Vector(-1, 3)
print(v1 * 3)               # output: Vector(6, 12)
print(v1 == Vector(2, 4))   # output: True
print(len(v1))              # output: 4 [as the norm ~ 4.47]
print(v1[0])                # output: 2 [x component]
print(v1[1])                # output: 4 [y component]
'''
