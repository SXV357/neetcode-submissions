# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode], l: float, r: float) -> bool:
            if not root:
                return True

            if not l < root.val < r:
                return False
            
            return helper(root.left, l, root.val) and helper(root.right, root.val, r)
        
        return helper(root, float('-inf'), float('inf'))