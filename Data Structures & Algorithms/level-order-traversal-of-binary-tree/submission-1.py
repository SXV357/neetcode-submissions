# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def dfs(self, root: Optional[TreeNode], level: int, elems: defaultdict(list)):
        if not root:
            return
        
        elems[level].append(root.val)

        self.dfs(root.left, level + 1, elems)
        self.dfs(root.right, level + 1, elems)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # just 1 node
        if root and not root.left and not root.right:
            return [[root.val]]
        
        elems = defaultdict(list[int])
        self.dfs(root, 0, elems)

        return list(elems.values())