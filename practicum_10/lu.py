import numpy as np
from numpy.typing import NDArray


def lu(A: NDArray, permute: bool) -> tuple[NDArray, NDArray, NDArray]:
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n, n))
    P = np.eye(n)
    for i in range(n):
        if permute:
            min_i = i
            for j in range(i + 1, n):
                if A[j, i] < A[min_i, i]:
                    min_i = j
            P[[i, min_i], :] = P[[min_i, i], :]

        for j in range(n):
            if i <= j:
                U[i][j] = (P @ A)[i][j] - (L[i, :] @ U[:, j])
            else:
                L[i][j] = ((P @ A)[i][j] - (L[i, :] @ U[:, j])) / U[j][j]

    return L, U, P
    

def solve(L: NDArray, U: NDArray, P: NDArray, b: NDArray) -> NDArray:
    n = L.shape[0]
    y = np.zeros((n, ))
    x = np.zeros((n, ))
    b = P @ b

    for i in range(n):
        y[i] = (b[i] - (L[i, :] @ y.T)) / L[i, i]

    for i in range(n-1, -1, -1):
        x[i] = (y[i] - (U[i, :] @ x.T)) / U[i, i]

    return x


def get_A_b(a_11: float, b_1: float) -> tuple[NDArray, NDArray]:
    A = np.array([[a_11, 1.0, -3.0], [6.0, 2.0, 5.0], [1.0, 4.0, -3.0]])
    b = np.array([b_1, 12.0, -39.0])
    return A, b


if __name__ == "__main__":
    # Let's implement the LU decomposition with and without pivoting
    # and check its stability depending on the matrix elements
    p = 14  # modify from 7 to 16 to check instability
    a_11 = 3 + 10 ** (-p)  # add/remove 10**(-p) to check instability
    b_1 = -16 + 10 ** (-p)  # add/remove 10**(-p) to check instability
    A, b = get_A_b(a_11, b_1)
    # print(A)
    # With pivoting
    L, U, P = lu(A, permute=True)
    x = solve(L, U, P, b)
    assert np.all(np.isclose(x, [1, -7, 4])), f"The anwser {x} is not accurate enough"
    # Without pivoting
    L, U, P = lu(A, permute=False)
    x_ = solve(L, U, P, b)
    assert np.all(np.isclose(x_, [1, -7, 4])), f"The anwser without pivoting {x_} is not accurate enough"
