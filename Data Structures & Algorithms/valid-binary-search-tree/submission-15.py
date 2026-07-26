# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode], left: float, right: float) -> bool:
        if not root:
            return True
        
        # this has gotta be true
        if not left < root.val < right:
            return False
        
        # for left traversal: root left bound < left.val < root.val
        # for right traversal: root.val < right.val < root right bound

        return self.dfs(root.left, left, root.val) and self.dfs(root.right, root.val, right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))