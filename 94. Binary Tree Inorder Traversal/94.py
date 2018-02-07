# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#法1：递归调用
class Solution:
    # 中序遍历，递归调用是很trivial的，先访问左孩子，
    # 读取当前节点的值，然后再遍历右孩子，按这个顺序即可

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.traversal(root, res)
        return res

    def traversal(self, node, res):
        if node:
            self.traversal(node.left, res)
            res.append(node.val)
            self.traversal(node.right, res)


# 法2：迭代
class Solution:
# 中序遍历，尝试用迭代思想
    
    def inorderTraversal(self, root):
        # 用栈来怼吧
        stack = []
        result = [] # 最后结果
        
        while True:
            # 先访问左孩子
            while root:
                stack.append(root)
                root = root.left
            
            if not stack:
                return result
            
            # 访问中间节点
            root = stack.pop()
            result.append(root.val)
           
            
            # 访问其右孩子
            root = root.right


