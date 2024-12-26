# 3286. Find a Safe Walk Through a Grid
# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/
import heapq
from typing import List

from common import ExampleInput, get_4_neighbors, execution_time


class Solution:
    @staticmethod
    @execution_time
    def find_safe_walk(grid: List[List[int]], health: int) -> bool:
        num_rows, num_cols = len(grid), len(grid[0])
        queue = []
        heapq.heappush(queue, (-health, 0, 0))
        visited = [[0] * num_cols for _ in range(num_rows)]

        while queue:
            node_health, r, c = heapq.heappop(queue)
            node_health = -node_health
            neighbor_health = node_health - grid[r][c]
            if neighbor_health < 1:
                continue
            elif r == num_rows - 1 and c == num_cols - 1:
                return True

            for neighbor in get_4_neighbors(grid, (r, c)):
                nr, nc = neighbor
                if visited[nr][nc] < neighbor_health:
                    heapq.heappush(queue, (-neighbor_health, nr, nc))
                    visited[nr][nc] = neighbor_health

        return False


if __name__ == "__main__":
    tc1 = ExampleInput(grid=[[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], health=1, output=True)
    tc2 = ExampleInput(grid=[[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0]], health=3,
                       output=False)
    tc3 = ExampleInput(grid=[[1, 1, 1], [1, 0, 1], [1, 1, 1]], health=5, output=True)
    tc4 = ExampleInput(grid=[[1, 1, 1, 1]], health=4, output=False)
    tc5 = ExampleInput(grid=[[1 for _ in range(50)] for _ in range(50)], health=99, output=False)

    result1 = Solution.find_safe_walk(tc1.grid, tc1.health)
    print(f"result1: {result1}")
    assert result1 == tc1.output

    result2 = Solution.find_safe_walk(tc2.grid, tc2.health)
    print(f"result2: {result2}")
    assert result2 == tc2.output

    result3 = Solution.find_safe_walk(tc3.grid, tc3.health)
    print(f"result3: {result3}")
    assert result3 == tc3.output

    result4 = Solution().find_safe_walk(tc4.grid, tc4.health)
    print(f"result4: {result4}")
    assert result4 == tc4.output

    # start_time5 = time.perf_counter()
    result5 = Solution.find_safe_walk(tc5.grid, tc5.health)
    print(f"result5: {result5}")
    assert result5 == tc5.output
