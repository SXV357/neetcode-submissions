# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
# 

from collections import defaultdict

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # building the map of indices so retrieving it is O(1)
        indices = defaultdict(int)
        for i, v in enumerate(inorder):
            indices[v] = i
        
        def helper(preorder_start, preorder_end, inorder_start, inorder_end):
            # prevent any sort of index out of bounds exceptions
            if preorder_start > preorder_end:
                return None

            curr_val = preorder[preorder_start]
            curr_node = TreeNode(curr_val)

            # O(1)
            mid = indices[curr_val]

            curr_node.left = helper(preorder_start + 1, preorder_start + (mid - inorder_start), inorder_start, mid - 1)
            curr_node.right = helper(preorder_start + (mid - inorder_start) + 1, preorder_end, mid + 1, inorder_end)

            # important otherwise we cannot return its root
            return curr_node
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)