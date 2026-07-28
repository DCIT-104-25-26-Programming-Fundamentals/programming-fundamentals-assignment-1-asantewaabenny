# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_matrix(matrix):
    """Displays a 2D matrix in a neatly aligned grid format."""
    for row in matrix:
        for val in row:
            print(f"{val:4}", end=" ")
        print()


def input_matrix(rows, cols, name="Matrix"):
    """Reads a matrix row by row from user input."""
    matrix = []
    print(f"\nEnter values for {name} ({rows}x{cols}):")
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


# -----------------------------------------------------------------------------
# PART A — Transpose Matrix
# -----------------------------------------------------------------------------
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create empty matrix of size cols x rows
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)
        
    return transposed


# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(matrix_a[r][c] + matrix_b[r][c])
        result.append(new_row)
        
    return result


# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            dot_product = 0
            for k in range(cols_a):
                dot_product += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(dot_product)
        result.append(new_row)
        
    return result


# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------
def main():
    print("=== PART A: Transpose Matrix ===")
    r1 = int(input("Enter number of rows: "))
    c1 = int(input("Enter number of columns: "))
    mat_a = input_matrix(r1, c1, "Matrix A")
    
    print("\nOriginal Matrix:")
    print_matrix(mat_a)
    
    print("\nTransposed Matrix:")
    transposed = transpose_matrix(mat_a)
    print_matrix(transposed)

    print("\n" + "="*40 + "\n")

    print("=== PART B: Add Matrices ===")
    print(f"Reading Matrix B of size {r1}x{c1}...")
    mat_b = input_matrix(r1, c1, "Matrix B")
    
    print("\nMatrix A + Matrix B:")
    sum_mat = add_matrices(mat_a, mat_b)
    print_matrix(sum_mat)

    print("\n" + "="*40 + "\n")

    print("=== PART C: Multiply Matrices ===")
    print(f"Matrix A is ({r1}x{c1}). Matrix C must have {c1} rows.")
    c2 = int(input("Enter number of columns for Matrix C: "))
    mat_c = input_matrix(c1, c2, "Matrix C")
    
    print("\nMatrix A x Matrix C:")
    prod_mat = multiply_matrices(mat_a, mat_c)
    print_matrix(prod_mat)


if __name__ == "__main__":
    main()