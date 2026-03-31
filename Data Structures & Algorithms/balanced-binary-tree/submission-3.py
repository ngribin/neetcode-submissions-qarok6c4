# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0 
        
    def height(self, root):
    
        if not root:
            return 0

        leftval = self.height(root.left)
        rightval = self.height(root.right)

        if leftval < 0 or rightval < 0 or abs(leftval - rightval) > 1:
            return -1

        return max(leftval, rightval) + 1
        
        