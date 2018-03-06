# 法1：定两头指针查找
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # 采用二分法去做
        # 刚开始一个指向0一个指向比sqrt(c)小的最大整数
        # 左指针直往后移，右指针只往前移
        p1, p2 = 0, int(math.sqrt(c))
        while p1 <= p2:
            if p1**2 + p2**2 > c:
                p2 -= 1
            elif p1**2 + p2**2 < c:
                p1 += 1
            else:
                return True
            
        return False

