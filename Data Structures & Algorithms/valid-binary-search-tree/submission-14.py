# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def bfs(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        
        q = deque([root])
        res = []

        while q:
            node = q.popleft()
            res.append(node.val)

            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
        
        return res
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        l_elems = self.bfs(root.left)
        r_elems = self.bfs(root.right)
        
        if not all(elem < root.val for elem in l_elems) or not all(elem > root.val for elem in r_elems):
            return False
        
        # everything on left and right is fine now we needa check subtrees also
        return self.isValidBST(root.left) and self.isValidBST(root.right)