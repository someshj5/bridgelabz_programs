import os

class Board:
    def __init__(self):
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def display(self):
        print(f'{self.cells[1]} | {self.cells[2]} | {self.cells[3]}')
        print('----------')
        print(f'{self.cells[4]} | {self.cells[5]} | {self.cells[6]}')
        print('----------')
        print(f'{self.cells[7]} | {self.cells[8]} | {self.cells[9]}')

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == ' ':
            self.cells[cell_no] = player
        else:
            print('\nAlready filled\n')
    def reset(self):
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


    def is_winner(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        elif self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True
        elif self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True
        elif self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        elif self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        elif self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True
        elif self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True
        elif self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            print('Won')
            return True
        return False
board = Board()

def header():
    print('Welcome to tic-tac-toe')

def refreshScreeen():
    return os.system('clear')

header()
board.display()

while True:
    x_choice = int(input('X Choose 1-9. >'))

    board.update_cell(x_choice, 'X')
    board.display()

    if board.is_winner('X'):
        print('\n X wins!\n')
        play_again = input('want to play again (Y,N)').upper()
        if play_again == 'Y':
            board.reset()
            continue

        else:
            break

    o_choice = int(input('O Choose 1-9. >'))
    board.update_cell(o_choice, 'O')
    refreshScreeen()
    board.display()

    if board.is_winner('O'):
        print('\n O wins!\n')
        play_again = input('want to play again (Y,N)').upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break


