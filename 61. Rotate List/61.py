# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        # 由于这个题目大于长度的数也成立，必须测量长度
        p, l = head, 1
        while p.next:
            l += 1
            p = p.next
        # 转化成有效数
        k %= l
        
        if k == 0 or not head.next:
            return head
    
        # 要确定被反向的开始元素
        # 初始化，将p1和p2之间形成k的间隔
        # 切断点p1距离末尾p2会有k的间隔，所以我们要这么初始化
        p1 = p2 = head
        while k > 0 and p2:
            p2 = p2.next
            k -= 1
        
        # # 如果p2已经到了最后了，那么就不进行任何操作
        # if not p2:
        #     return head
        
        # 把p1, p2移动到合适的位置
        while p2.next:
            p1 = p1.next
            p2 = p2.next
            
        
        # 此时p1的位置就是断点，p2指向最后一个元素，开始元素是p1后面那个
        p2.next, p1.next, head = head, None, p1.next
        
        return  head 
        
        