# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_queue = deque()
        if root:
            node_queue.append(root)
        
        result = []
        while len(node_queue):
            current_level_length = len(node_queue)
            current_result = []
            for i in range(current_level_length):
                current_node = node_queue.popleft()
                current_result.append(current_node.val)

                if current_node.left:
                    node_queue.append(current_node.left)
                if current_node.right:
                    node_queue.append(current_node.right)
            result.append(current_result)

        return result