from common import ExampleInput

// https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        if s[0] not in hash_map:
            return False
        open_stack = []
        for c in s:
            if c in hash_map:
                open_stack.append(hash_map[c])
            elif not open_stack or open_stack.pop() != c:
                return False

        return len(open_stack) == 0

if __name__ == '__main__':

    test_case1 = ExampleInput(s="()")
    test_case2 = ExampleInput(s="()[]{}")
    test_case3 = ExampleInput(s="(]")
    test_case4 = ExampleInput(s="([])")
    solution = Solution()

    test_result = solution.isValid(test_case1.s)
    print(test_result)
    assert test_result == True

    test_result2 = solution.isValid(test_case2.s)
    print(test_result2)
    assert test_result2 == True

    test_result3 = solution.isValid(test_case3.s)
    print(test_result3)
    assert test_result3 == False

    test_result4 = solution.isValid(test_case4.s)
    print(test_result4)
    assert test_result4 == True