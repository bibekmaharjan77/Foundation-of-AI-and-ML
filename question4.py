'''
Design Idea: 
- Compute determinant using recursion through Laplace Expansion (also called cofactor expansion).

Formula: det(A) = Σ(j=0 to n-1) (-1)^(0+j) x A[0,j] x det(M_0j)
    where M_0j is the minor (delete row 0, column j)

- For small matrices (2x2), use the explicit formula.

- For larger matrices, expand along first row.

Structure of the program:
Base case: 1x1 and 2x2 matrices.

Recursive case: for any n, expand and recurse on submatrices.

'''

# Just run the file by python3 question4.py

# Determinant via cofactor expansion
def matrix_determinant(matrix):
    '''Calculate the determinant of a square matrix (as a list of lists).'''
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for col in range(n):
        # Minor matrix
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        cofactor = ((-1) ** col) * matrix[0][col]
        det += cofactor * matrix_determinant(minor)
    return det

# Examples:
print(matrix_determinant([[1,2],[3,4]])) # -2
print(matrix_determinant([[1, 0, 2],[0,2,1],[3,1,1]])) # -11
