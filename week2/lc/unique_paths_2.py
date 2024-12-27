# 63. Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/description/?envType=study-plan-v2&envId=dynamic-programming
from typing import List

from common import ExampleInput, execution_time


class Solution:
    @execution_time
    def unique_paths_with_obstacles(self, obstacle_grid: List[List[int]]) -> int:
        num_rows, num_cols = len(obstacle_grid), len(obstacle_grid[0])
        if num_rows == 1:
            return 0 if any([num for row in obstacle_grid for num in row]) else 1
        if num_cols == 1:
            return 0 if any(obstacle_grid[0]) else 1
        if obstacle_grid[0][0] == 1 or obstacle_grid[-1][-1] == 1:
            return 0
        memo = {}

        def dfs(r: int, c: int) -> int:
            if r >= num_rows or c >= num_cols or obstacle_grid[r][c] == 1:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            if r == num_rows - 1 or c == num_cols - 1:
                return 1
            memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return memo[(r, c)]

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()
    tc1 = ExampleInput(grid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]], output=2)
    result1 = sol.unique_paths_with_obstacles(tc1.grid)
    print(f"Result 1: {result1}")
    assert result1 == tc1.output

    tc2 = ExampleInput(grid=[[0, 1], [0, 0]], output=1)
    result2 = sol.unique_paths_with_obstacles(tc2.grid)
    print(f"Result 2: {result2}")
    assert result2 == tc2.output

    tc3 = ExampleInput(grid=[[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]], output=5)
    result3 = sol.unique_paths_with_obstacles(tc3.grid)
    print(f"Result 3: {result3}")
    assert result3 == tc3.output

    tc4 = ExampleInput(grid=[[1]], output=0)
    result4 = sol.unique_paths_with_obstacles(tc4.grid)
    print(f"Result 4: {result4}")
    assert result4 == tc4.output

    tc5 = ExampleInput(grid=[[0, 0], [0, 1]], output=0)
    result5 = sol.unique_paths_with_obstacles(tc5.grid)
    print(f"Result 5: {result5}")
    assert result5 == tc5.output

    tc6 = ExampleInput(grid=[[0, 1, 0, 0]], output=0)
    result6 = sol.unique_paths_with_obstacles(tc6.grid)
    print(f"Result 6: {result6}")
    assert result6 == tc6.output
