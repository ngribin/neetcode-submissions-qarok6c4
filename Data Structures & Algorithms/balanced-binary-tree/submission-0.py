# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.Height(root) >= 0)
            

    def Height(self, root):
        if not root:
            return 0

        leftval = self.Height(root.left)
        rightval = self.Height(root.right)

        if leftval < 0 or rightval < 0 or abs(leftval - rightval) > 1:
            return -1
        return max(leftval, rightval)  + 1     

        