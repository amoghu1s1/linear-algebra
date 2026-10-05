import numpy as np

def solve_soe(A, b):
    try:
        return np.linalg.solve(A, b)  
    except np.linalg.LinAlgError:
        return "No unique solution exists."
    finally:
        print("Function ran successfully.")


def gaussian_elimination(A, b):
    n = len(A)

    augmented_matrix = np.column_stack((A, b))
    augmented_matrix = augmented_matrix.astype(float)

    for i in range(n):
        pivot_row = i
        max_value = abs(augmented_matrix[i][i])

        for k in range(i + 1, n):
            if abs(augmented_matrix[k][i]) > max_value:
                max_value = abs(augmented_matrix[k][i])
                pivot_row = k

        if pivot_row != i:
            augmented_matrix[[i, pivot_row]] = augmented_matrix[[pivot_row, i]]

        
        if abs(augmented_matrix[i][i]) < 1e-10:
            return "System has no unique solution"

        
        pivot = augmented_matrix[i][i]
        augmented_matrix[i] = augmented_matrix[i] / pivot

        
        for j in range(n):
            if j != i:                      
                factor = augmented_matrix[j][i]
                augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]

    
    return augmented_matrix[:, -1]


if __name__ == "__main__":
    A = np.array([[2., 1., -1.],
                  [-3., -1., 2.],
                  [-2., 1., 2.]])
    b = np.array([8., -11., -3.])

    print("NumPy solve   :", solve_soe(A, b))
    print("Gauss-Jordan  :", gaussian_elimination(A, b))