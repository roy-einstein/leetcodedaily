from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def pathSum(root: Optional[TreeNode], targetSum: int):
    if root is None:
        return False
    if root.right is None and root.left is None and targetSum == root.val:
        return True
    return pathSum(root.left, targetSum-root.val) or pathSum(root.right, targetSum-root.val)

if __name__ == "__main__":
    root = [5, 4, 8, 11, None, 13, 6, 7, 2, None, None, None, 1],
    targetSum = 21
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(8)
    d = TreeNode(11)
    e = TreeNode(13)
    f = TreeNode(6)
    g = TreeNode(7)
    h = TreeNode(2)
    i = TreeNode(1)
    a.left =b
    a.right =c
    b.left =d
    b.right =None
    c.left =e
    c.right=f
    f.right=i
    d.left=g
    d.right = h

    b = pathSum(a, targetSum)
    print(b)