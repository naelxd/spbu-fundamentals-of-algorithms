from typing import Callable
import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt


def lagrange_basis(i: int, x: float, x_nodes: NDArray):
    res1 = 1
    res2 = 1
    for j in range(len(x_nodes)):
        if (j == i):
            continue
        res1 *= (x - x_nodes[j])
        res2 *= (x_nodes[i] - x_nodes[j])

    return res1/res2

def lagrange_interpolant(x: float, x_nodes: NDArray, y_nodes: NDArray):
    li = np.empty(y_nodes.shape)
    for i in range(len(x_nodes)):
        li[i] = lagrange_basis(i, x, x_nodes)

    return y_nodes @ li

def plot_data_and_interpolant(x_nodes: NDArray, f: Callable[[float], float]):
    lnsp = np.linspace(x_nodes[0], x_nodes[-1], x_nodes.size * 10) 
    y_nodes = f(lnsp)
    y_interpolate = []
    for i in range(len(lnsp)):
        y_interpolate.append(lagrange_interpolant(lnsp[i], lnsp, y_nodes))
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(lnsp, y_nodes, "o")
    ax.plot(lnsp, y_interpolate, "-")
    ax.grid()
    fig.tight_layout()
    plt.show()

def runge_func(x: float) -> float:
    return 1.0 / (1 + 25 * x**2)


if __name__ == "__main__":
    # Let's implement optimal Lagrange interpolation and check it
    # on the Runge function

    # Equispaced nodes
    n = 11
    x_equi_nodes = np.linspace(-1.0, 1.0, n)
    plot_data_and_interpolant(x_equi_nodes, runge_func)

    # Optimally located nodes
    # Chebishovskiye uzli

    # plot_data_and_interpolant(x_opt_nodes, runge_func)
