def printboard(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
        
def valid(board, num, col, row):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    startrow, startcol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + startrow][j + startcol] == num:
                return False
    return True

def solver(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if valid(board, num, col, row):
                        board[row][col] = num
                        if solver(board):
                            return True
                        else:
                            board[row][col] = 0
                return False
    return True

def userinput():
    board = []
    print("Enter 9x9 sudoku grid. Use 0 for empty cells.")
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").split()))
                if len(row) == 9 and all( 0 <= num <= 9 for num in row):
                    board.append(row)
                    break
                else:
                    print("Invalid input. Please enter exactly 9 digits separated by spaces between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter exactly 9 digits separated by spaces between 0 and 9.")
    return board

if __name__ == "__main__":
    sudokuboard = userinput() 
    print("Initial board:")
    printboard(sudokuboard)
    
    if solver(sudokuboard):
        print("\nSolved board:")
        printboard(sudokuboard)
    else:
        print("No solution exists.")