from time import perf_counter

import numpy as np
from numpy.typing import NDArray

from src.plotting import plot_points

def is_clockwise_turn(a, b, c) -> bool:
    matrix = np.concatenate((np.array([a, b, c]), np.ones((1, 3)).T), axis=1)
    return np.linalg.det(matrix) > 0


def convex_bucket(points: NDArray) -> NDArray:
    """Complexity: O(n log n)"""
    clockwise_sorted_ch = []
    sorted_points_by_x = sorted(points, key=lambda x: (x[0], x[1]))

    for point in reversed(sorted_points_by_x):
        while (len(clockwise_sorted_ch) >= 2 and 
               not is_clockwise_turn(clockwise_sorted_ch[-2], 
                                     point, clockwise_sorted_ch[-1])):
            clockwise_sorted_ch.pop(-1)
        clockwise_sorted_ch.append(point)

    clockwise_sorted_ch += clockwise_sorted_ch[-2::-1]
    return np.array(clockwise_sorted_ch)


if __name__ == "__main__":
    for i in range(1, 11):
        txtpath = f"practicum_5/homework/points_{i}.txt"
        points = np.loadtxt(txtpath)
        print(f"Processing {txtpath}")
        print("-" * 32)
        t_start = perf_counter()
        ch = convex_bucket(points)
        t_end = perf_counter()
        print(f"Elapsed time: {t_end - t_start} sec")
        plot_points(points, convex_hull=ch, markersize=20)
        print()
