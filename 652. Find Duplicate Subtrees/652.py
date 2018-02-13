# 使用哈希表

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution(object):
    def findDuplicateSubtrees(self, root):
        def preTra(node):  # node是当前节点，tree是字典用来保存树结构
            if not node:
                return 'null'
            structure = "%s,%s,%s" % (str(node.val), preTra(node.left),
                                      preTra(node.right))
            tree[structure].append(node)
            return structure

        tree = collections.defaultdict(list)
        preTra(root)

        # 重复的只用读取一个就可以了
        return [
            tree[structure][0] for structure in tree
            if len(tree[structure]) > 1
        ]

d = collections.defaultdict(list)
d['1'].append(1)
d['1'].append(2)
d['2'].append(3)
print(d)