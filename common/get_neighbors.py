from typing import List, Tuple


def get_4_neighbors(grid: List[List[int]], point: Tuple[int, int]) -> List[Tuple[int, int]]:
    num_rows, num_cols = len(grid), len(grid[0])
    row, col = point
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    res = []
    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]
        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
            res.append((neighbor_row, neighbor_col))
    return res


def get_8_neighbors(grid: List[List[int]], point: Tuple[int, int]) -> List[Tuple[int, int]]:
    num_rows, num_cols = len(grid), len(grid[0])
    row, col = point
    delta_row = [-1, 0, 1, 0, -1, 1, 1, -1]
    delta_col = [0, 1, 0, -1, 1, 1, -1, -1]
    res = []
    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]
        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
            res.append((neighbor_row, neighbor_col))
    return res
