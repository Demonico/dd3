from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        assert isinstance(next, Optional[ListNode])
        self.next = next