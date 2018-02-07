# 法1：递归调用

class Solution:
    def preorderTraversal(self, root):
        res = []
        self.Traversal(root, res)
        return res
    
    def Traversal(self, root, res):
        if root:
            res.append(root.val)
            self.Traversal(root.left, res)
            self.Traversal(root.right, res)


# 法2：迭代法，类似94题中序遍历
class Solution:
    def preorderTraversal(self, root):
        res, stack = [], []
        
        while True:
            # 先根节点，直接读取值，然后再访问左节点，直至左节点没有了，访问右节点
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.left
                
            if not stack:
                return res

            root = stack.pop()
            # 最后右孩子，指向右孩子还是先读取值再左孩子
            root = root.right     