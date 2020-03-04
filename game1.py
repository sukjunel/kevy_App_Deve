#TicTacToe
import numpy as np


def print_board(matrix):
    for i in range(len(matrix)):
        print("-------")
        for j in range(len(matrix)):
            print("|", end='')
            print(matrix[i][j], end='')
        print('|')
    print("-------")

def valid_input(in1, in2, matrix):
    valid = True
    if int(in1) < 1 or int(in1) >3 or int(in2) < 1 or int(in2) > 3:
        print("Invalid input. Please try again Sir.")
        valid = False

    elif matrix[int(in1)-1][int(in2)-1] != ' ':
        print("space taken. Please try again Sir.")
        valid = False
    return valid

def winner(matrix):
    carryon = True
    if (matrix[0][0] and matrix[0][1] and matrix[0][2] == 'X' ) or (matrix[1][0] and matrix[1][1] and matrix[1][2] == 'X') or (matrix[2][0] and matrix[2][1] and matrix[2][2] == 'X'):
        print("You win!!!")
        carryon = False
    else:
        carryon = True
    return carryon


def board_full(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][i] != ' ':
                count = count+1
    return count

if __name__ == "__main__":

    board = np.full((3,3), " ")
    print_board(board)
    print("Welcome to June(석준)s TicTacToe Game")

    while True:
        while True:
            print("Enter the row(1-3): ", end='')
            row_in = input()
            print("Enter the col(1-3): ", end='')
            col_in = input()
            valid_input(row_in, col_in, board)
            if(valid_input(row_in, col_in, board) == True):
                break

        board[int(row_in) - 1][int(col_in) - 1] = 'X'
        print_board(board)
        if (board_full(board) == 9) or (winner(board) == False):
            break
    print("Game end. Adios Amigo Mate :)")