import numpy as np

def input_matrix(matrix_name):
    print(f"Enter the dimensions of matrix {matrix_name} (rows and columns):")
    rows, columns = map(int, input().split())

    matrix = []
    print(f"Enter the elements of matrix {matrix_name}, row by row:")
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    return np.array(matrix)

def my_print(A, B, P_a, P_b, i):
    print("\n================================\niteration = ", i, "\n================================")
    print(f"Matrix A:\n", A, "\n================================")
    print(f"P", P_a, "\n================================")
    print(f"Matrix B:\n", B, "\n================================")
    print(f"P", P_b, "\n")

def get_p(A, B):
    AB = np.vstack((A, B))
    n = AB.shape[0]
    p = [0] * n
    current_id = 1

    for i in range(n):
        if p[i] == 0:
            p[i] = current_id
            row_i_sorted = sorted(AB[i])
            for j in range(i + 1, n):
                if sorted(AB[j]) == row_i_sorted:
                    p[j] = current_id
            current_id += 1
    p_A = np.array(p[:A.shape[0]]).reshape(-1, 1)
    p_B = np.array(p[A.shape[0]:]).reshape(-1, 1)
    return [np.transpose(p_A), np.transpose(p_B)]

def s(matrix, p):
    P = np.array(p)
    P = np.transpose(P)
    matrix_new = matrix.copy()
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] == 0:
                matrix_new[i][j] = matrix[i][j] * 100
            else:
                matrix_new[i][j] = matrix[i][j] * 100 + P[i] * 10 + P[j]
    return matrix_new

def main(num_iterations):
    # print("Enter matrix A:")
    # A = input_matrix('A')
    # print("Enter matrix B:")
    # B = input_matrix('B')
    A = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 2, 1, 0, 0],
              [0, 0, 1, 0, 0, 0, 2, 0],
              [0, 0, 10, 0, 0, 0, 0, 0],
              [0, 2, 0, 10, 0, 1, 1, 0],
              [0, 1, 0, 0, 1, 0, 10, 1],
              [0, 0, 2, 0, 1, 0, 0, 1],
              [0, 0, 0, 0, 0, 1, 1, 0]])

    # Matrix B
    B = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 1, 10, 1, 2, 0],
                [0, 1, 1, 0, 0, 0, 0, 2],
                [0, 0, 0, 0, 0, 0, 0, 10],
                [0, 1, 1, 10, 0, 0, 1, 0],
                [0, 0, 2, 0, 0, 1, 0, 0],
                [0, 0, 0, 2, 0, 0, 0, 1]])
    p_A, p_B = get_p(A, B)
    my_print(A, B, p_A, p_B, 0)

    for i in range(num_iterations):
        A_new, B_new = s(A, p_A), s(B, p_B)
        p_A, p_B = get_p(A_new, B_new)
        my_print(A_new, B_new, p_A, p_B, i+1)

main(3)