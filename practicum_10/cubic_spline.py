import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt


def qubic_spline_coeff(x_nodes: NDArray, y_nodes: NDArray) -> NDArray:
    hi = [x_nodes[i+1] - x_nodes[i] for i in range(x_nodes.size - 1)]
    b = [(3/hi[i])*(y_nodes[i+1] - y_nodes[i]) - (3/hi[i-1])*(y_nodes[i] - y_nodes[i-1]) if 0 < i < x_nodes.size - 2 else 0 for i in range(x_nodes.size)]
    a = np.zeros((x_nodes.size, x_nodes.size)) 
    a[0, 0] = 1
    a[x_nodes.size-1, x_nodes.size-1] = 1
    for i in range(1, x_nodes.size-1):
        a[i][i-1] = hi[i-1]
        a[i][i] = 2*(hi[i] + hi[i-1])
        a[i][i+1] = hi[i]
    a_inv = np.linalg.inv(a)
    ci = a_inv @ np.array(b)
    di = [(ci[i+1] - ci[i]) / (3 * hi[i]) for i in range(x_nodes.size - 1)]
    bi = [(y_nodes[i+1] - y_nodes[i]) / hi[i] - ((hi[i] / 3) * (ci[i+1] + 2*ci[i])) for i in range(x_nodes.size)]
    print(len(bi), ci.shape, len(di))
    return np.concatenate((y_nodes, bi, ci, di), axis=1)

def qubic_spline(x: float, x_nodes: NDArray, qs_coeff: NDArray) -> float:
    for i in range(x_nodes.size):
        if x < x_nodes[i]:
            break
    i -= 1

    return (qs_coeff[i][0] + qw_coeff[i][1] * (x - x_nodes[i]) + 
            qw_coeff[i][2] * (x - x_nodes[i])**2 + 
            qw_coeff[i][3] * (x - x_nodes[i])**3)


if __name__ == "__main__":
    # Let's build a cubic spline and use it to interpolate GRP

    gdp = np.array(
        [
            506500154001.466,
            516814258695.568,
            517962962962.963,
            460290556900.726,
            435083713850.837,
            395077301248.464,
            395531066563.296,
            391719993756.828,
            404926534140.017,
            270953116950.026,
            195905767668.562,
            259708496267.33,
            306602673980.117,
            345110438692.185,
            430347770731.787,
            591016690742.798,
            764017107992.391,
            989930542278.695,
            1299705247685.76,
            1660844408499.61,
            1222643696991.85,
            1524916112078.87,
            2031768558635.85,
            2170143623037.67,
            2230625004653.55,
            2063662281005.13,
            1365865245098.18,
            1283162348132.8,
        ]
    )
    years = np.arange(1989.0, 2017.0)
    x = np.linspace(years[0], years[-1], 500)
    coeff = qubic_spline_coeff(years, gdp)
    spline_vectorized = np.vectorize(qubic_spline, excluded=set((1, 2)))
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    ax.plot(years, gdp, "x", markersize=10)
    ax.plot(x, spline_vectorized(x, years, coeff))
    ax.grid()
    plt.show()
