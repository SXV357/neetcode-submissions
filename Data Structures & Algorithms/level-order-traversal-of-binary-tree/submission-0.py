# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def bfs_recursive(self, root: Optional[TreeNode], level: int, elems: defaultdict(list)):
        if not root:
            return
        
        elems[level].append(root.val)

        self.bfs_recursive(root.left, level + 1, elems)
        self.bfs_recursive(root.right, level + 1, elems)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # just 1 node
        if root and not root.left and not root.right:
            return [[root.val]]
        
        elems = defaultdict(list[int])
        self.bfs_recursive(root, 0, elems)

        return list(elems.values())