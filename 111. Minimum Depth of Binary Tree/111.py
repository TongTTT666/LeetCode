# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # BFS is a good way to find the depth of a binary tree!
        # Use queue to do BFS
        queue = []
        # record the node and its depth like (root, 3)
        queue.append((root, 1))
        
        while queue:
            (node, depth) = queue.pop(0)
            # If it is a leaf node, its depth must be the shortest one because of BFS.
            if not node.left and not node.right:
                return depth 
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
            
            
        