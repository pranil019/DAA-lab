def isSafe(board, row, col, num):

    # check row
    for x in range(9):
        if board[row][x] == num:
            return False

    # check column
    for x in range(9):
        if board[x][col] == num:
            return False

    # check 3x3 box
    startRow = row - row % 3
    startCol = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False

    return True


def solveSudoku(board):

    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:

                for num in range(1, 10):

                    if isSafe(board, row, col, num):

                        board[row][col] = num

                        if solveSudoku(board):
                            return True

                        board[row][col] = 0   # backtrack

                return False

    return True


# INPUT
print("Enter Sudoku row by row (use 0 for empty):")

board = []
for i in range(9):
    row = list(map(int, input().split()))
    board.append(row)

# SOLVE OUTPUT
if solveSudoku(board):
    print("\nSolved Sudoku:")
    for row in board:
        print(row)
else:
    print("No solution exists")
