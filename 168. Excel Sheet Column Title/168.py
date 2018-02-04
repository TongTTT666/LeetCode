class Solution:
    def convertToTitle(self, n):
        # 相当于10进制转27进制
        # 一道纯数学题，并非考到算法
        # 用短除法进行转换记录每一个余数
        Excel_sheet = ""
        flag = 0
        while n > 0:
            temp = n % 26 - flag # 余数，需要修正
            n = n // 26 # 除数
            if temp == 0:
                c = 'Z'
                flag = 1
            else:
                flag = 0
                c = chr(ord('A') + temp - 1)
            Excel_sheet = c + Excel_sheet
            if n == 1 and temp == 0:  # 最奇葩的一种状态就是余数为0最后商为1，这种情况结束
                break
            
        return Excel_sheet