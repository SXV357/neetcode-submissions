# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def dfs(self, root: Optional[TreeNode], res: List[int]) -> list[int]:
        if not root:
            return []
        
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [] 
        self.dfs(root, res)

        return res[k-1]