from time import perf_counter
from queue import Queue


class Maze:
    def __init__(self, list_view: list[list[str]]) -> None:
        self.list_view = list_view
        self.start_j = None
        for j, sym in enumerate(self.list_view[0]):
            if sym == "O":
                self.start_j = j

    @classmethod
    def from_file(cls, filename):
        list_view = []
        with open(filename, "r") as f:
            for l in f.readlines():
                list_view.append(list(l.strip()))
        obj = cls(list_view)
        return obj

    def is_end(self, i: int, j: int) -> bool:
        return self.list_view[i][j] == "X"

    def print(self, path="") -> None:
        # Find the path coordinates
        i = 0  # in the (i, j) pair, i is usually reserved for rows and j is reserved for columns
        j = self.start_j
        path_coords = set()
        for move in path:
            i, j = _shift_coordinate(i, j, move)
            path_coords.add((i, j))
        # Print maze + path
        for i, row in enumerate(self.list_view):
            for j, sym in enumerate(row):
                if (i, j) in path_coords:
                    print("+ ", end="")  # NOTE: end is used to avoid linebreaking
                else:
                    print(f"{sym} ", end="")
            print()  # linebreak


def solve(maze: Maze) -> None:
    path = ""  # solution as a string made of "L", "R", "U", "D"

    queue = Queue()
    queue.put(path)
    i_size, j_size = len(maze.list_view), len(maze.list_view[0])
    is_visited = [[False] * j_size for _ in range(i_size)]

    while not queue.empty():
        path = queue.get()

        i, j = get_new_coords(0, maze.start_j, path)

        if (i > i_size - 1 or j > j_size - 1) or (i, j) == (-1, -1) or is_visited[i][j]:
            continue

        is_visited[i][j] == True

        if maze.is_end(i, j):
            break

        if maze.list_view[i][j] != '#':
            for way in 'L', 'R', 'U', 'D':
                queue.put(path + way)

    print(f"Found: {path}")
    maze.print(path)

def get_new_coords(i: int, j: int, path: str) -> tuple[int, int]:
    for way in path:
        new_i, new_j = _shift_coordinate(i, j, way)
        if new_i < 0 or new_j < 0:
            return (-1, -1)
        i, j = new_i, new_j
    return (i, j)

def _shift_coordinate(i: int, j: int, move: str) -> tuple[int, int]:
    if move == "L":
        j -= 1
    elif move == "R":
        j += 1
    elif move == "U":
        i -= 1
    elif move == "D":
        i += 1
    return i, j


if __name__ == "__main__":
    maze = Maze.from_file("practicum_2/homework/maze_2.txt")
    t_start = perf_counter()
    solve(maze)
    t_end = perf_counter()
    print(f"Elapsed time: {t_end - t_start} sec")
