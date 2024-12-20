from typing import Optional

from common import ExampleInput, ListNode


# https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        if list1.val < list2.val:
            list1.next = self.merge_two_lists(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_two_lists(list1, list2.next)
            return list2


if __name__ == "__main__":
    test_case1 = ExampleInput(list1=ListNode.from_list([1, 2, 4]), list2=ListNode.from_list([1, 3, 4]))
    solution = Solution()
    test_result1 = solution.merge_two_lists(test_case1.list1, test_case1.list2)
    print(f"test_result1: {ListNode.to_list(test_result1)}")
    assert ListNode.to_list(test_result1) == [1, 1, 2, 3, 4, 4]
