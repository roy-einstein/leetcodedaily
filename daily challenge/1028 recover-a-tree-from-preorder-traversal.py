"""
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.



Example 1:


Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:


Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
Example 3:


Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]


Constraints:

The number of nodes in the original tree is in the range [1, 1000].
1 <= Node.val <= 109
"""
from collections import deque, defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        t= traversal

        stk =[]
        i=0
        while i<n:
            lvl=0
            while i<n and t[i] == '-':
                lvl +=1
                i +=1
            j=i
            while j<n and t[j].isdigit():
                j +=1

            val = int(t[i:j])
            i=j
            node  = TreeNode(val)
            while len(stk) > lvl:
                stk.pop()
            if stk:
                if stk[-1].left is None:
                    stk[-1].left =node
                else:
                    stk[-1].right = node
            stk.append(node)
        return stk[0]


if __name__ == '__main__':
    s="1-2--3--4-5--6--7"
    b = Solution().recoverFromPreorder(s)





