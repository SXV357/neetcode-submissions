# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
            
        first = preorder[0]

        root = TreeNode(first)
        inorder_idx = inorder.index(first)

        left_side = inorder[:inorder_idx]
        right_side = inorder[inorder_idx + 1:]

        preorder_left = preorder[1:1+len(left_side)]
        preorder_right = preorder[1+len(left_side):]

        root.left = self.buildTree(preorder_left, left_side)
        root.right = self.buildTree(preorder_right, right_side)

        return root