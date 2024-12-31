from collections import deque
from typing import Optional


# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/description/

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def clone_graph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        q = deque([node])
        cloned = {node.val: Node(node.val, [])}

        while q:
            cur_node = q.popleft()
            cur_clone = cloned[cur_node.val]

            for nbr in cur_node.neighbors:
                if nbr.val not in cloned:
                    cloned[nbr.val] = Node(nbr.val, [])
                    q.append(nbr)

                cur_clone.neighbors.append(cloned[nbr.val])

        return cloned[node.val]

# Note: The output of this one is essentially the input but you have to build new nodes.
