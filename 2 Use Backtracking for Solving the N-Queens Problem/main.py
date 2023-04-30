def is_valid(board, row, col, N):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check if there is a queen in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check if there is a queen in the lower left diagonal
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, row, N):
    if row == N:
        return True
    for col in range(N):
        if is_valid(board, row, col, N):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, N):
                return True
            board[row][col] = 0
    return False

# Testing the algorithm with board size 4
N = 4
board = [[0 for _ in range(N)] for _ in range(N)]
if solve_n_queens(board, 0, N):
    for row in board:
        print(row)
else:
    print("No solution found.")

#In this implementation, the board is represented as a 2D list of integers, 
#where 0 represents an empty cell and 1 represents a cell containing a queen. 
#The is_valid() function checks if it is safe to place a queen in a given cell by checking the row, 
#column, and diagonals for other queens. The solve_n_queens() function is a recursive function that 
#solves the N-Queens problem using Backtracking. It starts by checking if all rows have been filled with a queen. 
#If not, it tries to place a queen in each column of the current row and checks if it is safe to do so using the is_valid() function. 
#If a safe cell is found, it marks the cell as a queen and moves on to the next row recursively. 
#If all rows have been filled with a queen, it returns True to indicate that a solution has been found.
# If it is not possible to place a queen in the current row and all subsequent rows, it backtracks to the previous 
#row by removing the queen from the current cell and trying the next column in the previous row. 
#If all columns in the current row have been tried and none of them lead to a solution, it returns False 
#to indicate that no solution has been found.
