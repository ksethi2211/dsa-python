# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        def dfs(left: TreeNode, right: TreeNode, is_root: bool) -> bool:
            if is_root:
                return dfs(left.left, left.right, False)
            
            if left == None and right == None:
                return True
            
            if (left == None and right != None) or (left != None and right == None) or (left.val != right.val):
                return False
            
            result = True
            if left.left != None and right.right != None:
                result = dfs(left.left, right.right, False)
            elif left.left == None and right.right == None:
                result = True
            else:
                result = False
            
            if not result:
                return False
            
            if left.right != None and right.left != None:
                result = dfs(left.right, right.left, False)
            elif left.right == None and right.left == None:
                result = True
            else:
                result = False
            
            return result
        
        return dfs(root, None, True)

            
