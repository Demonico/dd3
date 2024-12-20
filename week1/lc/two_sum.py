from common import ExampleInput

# https://leetcode.com/problems/two-sum/description/
class Solution:
    @staticmethod
    def two_sum(nums, target):
        compliments = {}

        for i, num in enumerate(nums):
            if num in compliments:
                return [compliments[num], i]
            compliments[target - num] = i
        print(hmap.items())
        return []


if __name__ == '__main__':
    test_case1 = ExampleInput(nums=[2, 7, 11, 15], target=9)
    test_case2 = ExampleInput(nums=[3,2,4], target=6)
    test_case3 = ExampleInput(nums=[3,3], target=6)
    test_case4 = ExampleInput(nums=[-1,-2,-3,-4,-5], target=-8)

    test_result1 = Solution.two_sum(test_case1.nums, test_case1.target)
    print(test_result1)
    assert test_result1 == [0,1]

    test_result2 = Solution.two_sum(test_case2.nums, test_case2.target)
    print(test_result2)
    assert test_result2 == [1,2]

    test_result3 = Solution.two_sum(test_case3.nums, test_case3.target)
    print(test_result3)
    assert test_result3 == [0,1]

    test_result4 = Solution.two_sum(test_case4.nums, test_case4.target)
    print(test_result4)
    assert test_result4 == [2,4]