import heapq
import math
from typing import List

from common import ExampleInput


# LC 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/description/


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
                    loop over points
                        calculate distance and add point with distance to heap, prioritized by dist
                    return k closest from heap
                """
        h = [(math.sqrt(point[0] ** 2 + point[1] ** 2), point) for point in points]
        return [point for _, point in heapq.nsmallest(k, h)]


if __name__ == "__main__":
    tc1 = ExampleInput(points=[[1, 3], [-2, 2]], k=1, output=[[-2, 2]])
    tc2 = ExampleInput(points=[[3, 3], [5, -1], [-2, 4]], k=2, output=[[3, 3], [-2, 4]])
    sol = Solution()

    result1 = sol.kClosest(tc1.points, tc1.k)
    assert result1 == tc1.output

    result2 = sol.kClosest(tc2.points, tc2.k)
    assert result2 == tc2.output
