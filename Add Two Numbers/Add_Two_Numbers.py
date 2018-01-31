# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 创建根节点，不能改变root的指针，必须指在开头
        # 但是我们又必须要对这个List做出改变，那么就再创建一个指针temp指向该List
        # 通过操纵temp指针从而完成最终的目的，能够保证root指针不变
        root = temp = ListNode(0)
        # carry 是进位，有进位也要继续算
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            # 确定下一次的进位
            if sum <= 9:
                carry = 0
            else:
                carry = 1
                sum -= 10

            temp.next = ListNode(sum)
            temp = temp.next

        return root.next
