# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        
        if not head:
            return
    
        # 1. 找到中间点，准备进行后半部分的节点颠倒
        temp1 = temp2 = head
        while temp2 and temp2.next:
            temp1, temp2 = temp1.next, temp2.next.next
        # 此时，temp1所指的下一个节点，就是中间节点，也就是从这个节点开始
        # 后面所有的节点反向。
        mid = temp1
        
        
        #2. 将后一半节点颠倒，为了方便下一步的插入，需要三个指针
        current_node, last_node = mid, None
        
        while current_node:
            # 作用过程
            next_node, current_node.next = current_node.next, last_node
            # 传递过程
            last_node, current_node = current_node, next_node           
            
            
        # 3. 按照规定的顺序插入，得到最后结果，肯定需要两个指针，现在已经反向了
        # 最后一个就是反排序的第一个，最后一个节点是last_node
        temp1, temp2= head, last_node
        
        while temp2.next:          
        
            # python简便编法
            # temp1.next, temp1 = temp2, temp1.next
            # temp2.next, temp2 = temp1, temp2.next
            # 传统编法
            p1 = temp1.next
            temp1.next = temp2
            p2 = temp2.next
            temp1 = p1
            temp2.next = temp1
            temp2 = p2
     
        return
    
        
        
        
        
        
        
        
       
        
        
        
            
        
        
    