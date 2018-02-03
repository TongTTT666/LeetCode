# 法1：98ms
class Solution:
    def reverse(self, x):
        # 不能超过32位
        if x < -0x7fffffff or x > 0x7fffffff-1:
            return 0
        # 最关键的问题，将原始数据转换成list方便
        num = str(x)
        num = list(num)
        # 计算数字位数
        length = len(num)
        # 下面还要分是正是负取怼，负数就先不考虑负号嘛，长度减1
        if num[0] == '-':
            length -= 1
            num = num[1:]
            flag = 0
        else:
            flag = 1
        # 分奇偶取中间元素，然后两边推进交换元素
        if length % 2 == 1: # odd
            k1 = k2 = (length+1)//2 - 1
        else:
            k1 = (length+1)//2 - 1
            k2 = (length+1)//2
        # 从中间往两边推，交换元素
        while k1 >= 0 and k2 < length:
            num[k1], num[k2] = num[k2], num[k1] 
            k1 -= 1
            k2 += 1
        
        if num[0] == 0:
                num = num[1:]
        
        num = ''.join(num)
        num = int(num)
        
        # 32位限制
        if num < -0x7fffffff or num > 0x7fffffff-1:
            return 0
        else:
            if flag == 1:
                return num
            else:  # 负数直接加负号就行了啊
                return -num
        