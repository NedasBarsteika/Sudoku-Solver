def find_next_empty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col
            
    return None, None

def is_valid(puzzle, row, col, guess):
    # Checks row
    for x in range(9):
        if puzzle[row][x] == guess:
            return False
        
    # Checks column
    for x in range(9):
        if puzzle[x][col] == guess:
            return False
        
    # Checks 3 x 3 square
    startRow = row - row % 3
    startCol = col - col % 3
    for r in range(startRow, startRow + 3):
        for c in range(startCol, startCol + 3):
            if puzzle[r][c] == guess:
                return False
            
    return True
        

def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    if row == None:
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle, row, col, guess):
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True
        
        puzzle[row][col] = 0

    return False

def print_puzzle(puzzle):
    for row in range(9):
        for col in range(9):
            print(puzzle[row][col], end=" ")
        print()

puzzle = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
          [0, 1, 0, 0, 0, 4, 0, 0, 0],
          [4, 0, 7, 0, 0, 0, 2, 0, 8],
          [0, 0, 5, 2, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 9, 8, 1, 0, 0],
          [0, 4, 0, 0, 0, 3, 0, 0, 0],
          [0, 0, 0, 3, 6, 0, 0, 7, 2],
          [0, 7, 0, 0, 0, 0, 0, 0, 3],
          [9, 0, 3, 0, 0, 0, 6, 0, 4]]

if solve_sudoku(puzzle):
    print_puzzle(puzzle)
else:
    print("Puzzle has no solution")