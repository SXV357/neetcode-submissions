# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def is_same_tree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if not t1 and not t2:
            return True
        
        if (t1 and not t2) or (t2 and not t1):
            return False
        
        if t1.val != t2.val:
            return False
        
        return self.is_same_tree(t1.left, t2.left) and self.is_same_tree(t1.right, t2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        check = self.is_same_tree(root, subRoot)

        if check:
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        