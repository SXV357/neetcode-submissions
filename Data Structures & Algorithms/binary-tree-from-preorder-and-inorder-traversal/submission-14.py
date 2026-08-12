# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = defaultdict(int)
        for i, val in enumerate(inorder):
            indices[val] = i

        def helper(preorder_start, preorder_end, inorder_start, inorder_end):
            if preorder_start > preorder_end:
                return None

            root_val = preorder[preorder_start]
            root = TreeNode(root_val)

            mid = indices[root_val]
            num_left = mid - inorder_start
            
            root.left = helper(preorder_start + 1, preorder_start + num_left, inorder_start, mid - 1)
            root.right = helper(preorder_start + num_left + 1, preorder_end, mid + 1, inorder_end)

            return root
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
