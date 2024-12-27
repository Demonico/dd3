from typing import List

from common import ExampleInput, execution_time


# 740. Delete and Earn
# https://leetcode.com/problems/delete-and-earn/description/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    @execution_time
    def delete_and_earn(self, nums: List[int]) -> int:
        max_num = max(nums) + 1
        points = [0] * max_num

        for num in nums:
            points[num] += num

        prev2, prev1 = 0, points[1]
        for i in range(2, max_num):
            tmp = max(prev1, prev2 + points[i])
            prev2 = prev1
            prev1 = tmp

        return prev1


if __name__ == "__main__":
    sol = Solution()
    tc1 = ExampleInput(nums=[3, 4, 2], output=6)
    result1 = sol.delete_and_earn(tc1.nums)
    print(f"Result 1: {result1}")
    assert result1 == tc1.output

    tc2 = ExampleInput(nums=[2, 2, 3, 3, 3, 4], output=9)
    result2 = sol.delete_and_earn(tc2.nums)
    print(f"Result 2: {result2}")
    assert result2 == tc2.output

    tc3 = ExampleInput(nums=[1], output=1)
    result3 = sol.delete_and_earn(tc3.nums)
    print(f"Result 3: {result3}")
    assert result3 == tc3.output

    tc4 = ExampleInput(nums=[10000], output=10000)
    result4 = sol.delete_and_earn(tc4.nums)
    print(f"Result 4: {result4}")
    assert result4 == tc4.output
