# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        self.Tiltofbinarytree = 0
        
        def Tilt_sum(node):
            if not node:
                return 0
            left = Tilt_sum(node.left)
            right = Tilt_sum(node.right)

            self.Tiltofbinarytree += abs(left - right)

            return left + right + node.val
    
        Tilt_sum(root)
        
        return self.Tiltofbinarytree