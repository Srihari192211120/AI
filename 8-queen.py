def print_board(board):
    """Helper function to print the board"""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    n = len(board)
    # Check this row on the left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, col, step_counter):
    """Use backtracking to find one solution"""
    n = len(board)
    if col >= n:
        print_board(board)
        return True, step_counter

    for i in range(n):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1
            step_counter += 1
            print(f"Placing queen at ({i}, {col})")
            print_board(board)

            # Recur to place the rest of the queens
            solved, step_counter = solve_n_queens(board, col + 1, step_counter)
            if solved:
                return True, step_counter

            # If placing queen at board[i][col] doesn't lead to a solution,
            # then remove the queen (backtrack)
            board[i][col] = 0
            step_counter += 1
            print(f"Removing queen from ({i}, {col})")
            print_board(board)

    return False, step_counter

def solve(n):
    """Initialize the board and start the solving process"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    step_counter = 0
    solved, step_counter = solve_n_queens(board, 0, step_counter)
    if not solved:
        print("Solution does not exist")
    print(f"COST== {step_counter}")
    return

# Change the value of n to solve for different board sizes
n = 4
solve(n)
