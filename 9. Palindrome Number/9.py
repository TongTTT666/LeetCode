# 法1：531 ms
class Solution:
    def isPalindrome(self, x):
        # 尽可能不转换成字符串去处理
        # 提取第n位的值(x/10^n)%10
        # 如何判断一个数有几位？在不调用字符串的情况下
        # 负数不可能是回文，最后一位是0的也不可能是回文
        if x < 0 or x % 10 == 0 and x != 0:
            return False

        max_digit = 1
        min_digit = 1

        # 确定最大除数，也即10^n最大是多少，n也就知道了
        temp = x
        while temp >= 10:
            temp //= 10
            max_digit *= 10

        # 两边逼近判断是不是回文。。。
        while min_digit <= max_digit:
            if x // max_digit % 10 == x // min_digit % 10:
                max_digit //= 10
                min_digit *= 10
            else:
                return False
        return True


# 法2：485 ms
class Solution:
    def isPalindrome(self, x):
        # 第二种思路：比较一半的数字，用余数取出最后的数字
        # 用除数去掉原数的开头数字
        if x < 0 or x % 10==0 and x!=0: 
            return False
        sum = 0
        while x>sum:    
            sum = sum * 10 + x % 10
            x //= 10
        return (x==sum) or (x==sum//10)