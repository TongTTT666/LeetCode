# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # Only analysis the root node

        # bottom situation
        if not root:
            return
        
        # If the node's val is less than L, all its left children are not satisfy the condition 
        if root.val < L:
            # trim all left nodes
            return self.trimBST(root.right, L, R)
        # If the node's val is more than R, all its right children are not satisfy the condition
        elif root.val > R:
            # trim all right nodes
            return self.trimBST(root.left, L, R)
        else:
            # If the root node satisfy the condition, we shoule construct the BSF
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
        
        return root
        
