# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        node_queue = deque()
        if not root is None:
            node_queue.append(root)
        
        is_reverse = False
        while len(node_queue):
            current_result = []
            current_level_length = len(node_queue)
            for i in range(current_level_length):
                current_node = node_queue.popleft()
                current_result.append(current_node.val)
                if current_node.left:
                    node_queue.append(current_node.left)
                if current_node.right:
                    node_queue.append(current_node.right)

            if(is_reverse):
                current_result.reverse()
            result.append(current_result)
            is_reverse = not is_reverse

        return result