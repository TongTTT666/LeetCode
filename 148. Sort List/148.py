# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
            # 典型的merge sort问题
        def merge(h1, h2):
            # t_res是头指针
            res = t_res = ListNode(0) # 返回结果

            while h1 and h2:
                # 谁小放谁
                if h1.val < h2.val:
                    res.next = h1
                    h1 = h1.next
                else:
                    res.next = h2
                    h2 = h2.next
                res = res.next

            # 如果发现不是空的，直接把他后面的元素连过来
            # if h1:  # 如果h1不是空的
            #     res.next = h1
            # if h2:
            #     res.next = h2
            # 上述代码可以简化：
            res.next = h1 or h2

            return t_res.next
        
    
        # 是空或者只有一个元素
        if not head or not head.next:
            return head
        
        # 我们需要找到list的中点
        # 怎么找？一个指针移动1个单位，另外一个指针移动两个单位即可
        # P1移动1个单位，p2移动两个单位
        pre = p1 = p2 = head
        while p2 and p2.next:
            # 记录p1前面的位置，好截断
            pre, p1, p2 = p1, p1.next, p2.next.next
        # 当前p1指针就可以视为第2部分的开始，但我们
        # 必须还要切断它们之间的联系，用pre指针
        pre.next = None
        
        h1 = self.sortList(head)
        h2 = self.sortList(p1)
        
        res = merge(h1, h2)
        
        # 确认是merge中有问题
        return res
    
    
    
        
        