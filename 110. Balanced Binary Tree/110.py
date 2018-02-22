# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def DFS(node):
            # 如果是空集
            if not node:
                return 0
            
            leftdeep = DFS(node.left)
            rightdeep = DFS(node.right)
            
            # 根本不满足要求，直接滚蛋
            if abs(leftdeep - rightdeep) > 1 or leftdeep == -1 or rightdeep == -1:
                return -1
            # 暂时满足要求
            return 1 + max(leftdeep, rightdeep)
          
        return DFS(root) != -1