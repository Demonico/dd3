from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next:Optional[ListNode] = None):
        self.val = val
        assert isinstance(next, (ListNode, type(None)))
        self.next = next

    @classmethod
    def from_list(cls, nums: list):
        if not nums:
            return None
        head = ListNode(nums[0])
        node = head
        for num in nums[1:]:
            node.next = ListNode(num)
            node = node.next
        return head

    @classmethod
    def to_list(cls, head: ListNode) -> list:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums
