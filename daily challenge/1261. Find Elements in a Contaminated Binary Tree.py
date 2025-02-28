"""
Given a binary tree with the following rules:

root.val == 0
For any treeNode:
If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.


Example 1:


Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]);
findElements.find(1); // return False
findElements.find(2); // return True
Example 2:


Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False
Example 3:


Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True


Constraints:

TreeNode.val == -1
The height of the binary tree is less than or equal to 20
The total number of nodes is between [1, 104]
Total calls of find() is between [1, 104]
0 <= target <= 106
"""
from http.cookiejar import cut_port_re
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.val_to_node = set()

        def dfs(root, val):
            if not root:
                return val
            root.val=val
            self.val_to_node.add(val)
            dfs(root.root, 2*val +1)
            dfs(root.root, 2*val +2)
        dfs(root,0)

    def find(self, target: int) -> bool:
        return target in self.val_to_node

if __name__ == '__main__':
    root = TreeNode(-1)
    a = TreeNode(-1)
    b = TreeNode(-1)
    c = TreeNode(-1)
    d = TreeNode(-1)

    root.left = a
    root.right = b

    a.left =c
    a.right =d

    def display(root):
        stack = [root]
        result = []
        left, right = "left", "right"
        direction = left
        v_to_n ={0:0}
        current = root
        i=-1
        root.val =0
        while stack:
            node = stack.pop()
            node=node.left
            if node:
                stack.append(node)


    print(display(root))