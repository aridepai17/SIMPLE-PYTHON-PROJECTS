# Sudoku Solver

This is a Python program that solves a given Sudoku puzzle using backtracking. 
The program allows users to input the initial state of the Sudoku board and then solves the puzzle, if possible.

## Functions

### `printboard(board)`
This function prints the current state of the Sudoku board.

### `valid(board, num, col, row)`
This function checks if placing a number (`num`) at position (`row`, `col`) is valid.

### `solver(board)`
This is the backtracking function that solves the Sudoku puzzle.

### `userinput()`
This function takes user input for the initial state of the Sudoku board.

## How It Works

### Print the Sudoku Board
- The `printboard(board)` function iterates through each row and prints each cell separated by a space.

### Check Validity of a Number
- The `valid(board, num, col, row)` function checks if the number exists in the given row or column.
- It also checks if the number exists in the 3x3 sub-grid.

### Solve the Sudoku Puzzle
- The `solver(board)` function iterates through each cell in the board.
- For each empty cell (value 0), it tries placing numbers 1 to 9.
- It uses recursion to attempt to solve the puzzle.
- If placing a number leads to a solution, it returns `True`.
- If no number leads to a solution, it resets the cell to 0 and returns `False`.

### Input the Sudoku Puzzle
- The `userinput()` function prompts the user to enter each row of the Sudoku puzzle.
- Users should enter 9 digits separated by spaces, with `0` representing empty cells.

## Usage

1. Run the script.
2. Enter the Sudoku puzzle row by row. Use `0` for empty cells.
3. The script will display the initial board.
4. If the puzzle has a solution, it will display the solved board. If not, it will indicate that no solution exists.
