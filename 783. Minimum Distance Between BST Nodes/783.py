# 用中序遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDiffInBST(self, root):
        # 定义中序遍历函数
        def inorderTraversal(node):
            if node:
                inorderTraversal(node.left)
                self.node_mindif = min(node.val - self.pre, self.node_mindif)
                self.pre = node.val
                inorderTraversal(node.right)

        self.node_mindif = float('inf')
        self.pre = -float('inf')
        inorderTraversal(root)

        return self.node_mindif