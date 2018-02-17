# 法1：递归调用

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        res = []
        self.Traversal(root, res)
        return res
        
              
    def Traversal(self, root, res):
        if root:
            self.Traversal(root.left, res)
            self.Traversal(root.right, res)
            res.append(root.val)


# 法2： 迭代过程
# 入栈顺序: 左-》右 得值顺序：根=》右=》左=》 输出要反过来！

class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        
        res, stack = [], []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
       
        return res[::-1]
            