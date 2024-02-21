"""
3 9 20 15 7
9 3 15 20 7
if preorder length = 0
return None
preorder[0] = root
left = slice

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = preorder[0]
        i = inorder.index(root)
        left_inorder = inorder[:i]
        left_preorder = preorder[1:i+1]

        right_inorder = inorder[i+1:]
        right_preorder = preorder[i+1:]

        root_node = TreeNode(root)
        root_node.left = self.buildTree(left_preorder, left_inorder)
        root_node.right = self.buildTree(right_preorder, right_inorder)

        return root_node