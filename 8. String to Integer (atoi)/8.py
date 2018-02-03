# 法1：111 ms
class Solution:
    def myAtoi(self, str):
        if str == "":  # 空集合特殊情况
            return 0
        flag = 0  # 标志，表明正负数
        for index, c in enumerate(str):
            if c >= '0' and c <= '9' or c == '+' or c == '-':   # 出现关键字，进入下一个循环
                start = index
                end = start + 1
                if c >= '0' and c <= '9':
                    flag = 1
                    while(end < len(str)):
                        if str[end] >= '0' and str[end] <= '9':
                            end += 1
                        else:
                            break
                elif c == '+':  # 加号情形
                    flag = 1
                    while(end < len(str)):
                        if str[end] >= '0' and str[end] <= '9':
                            end += 1
                        else:
                            break
                    start += 1 # 符号位要去掉分析
                    if start == end:  # 这个符号后面又跟了一个非法字符，放弃
                        return 0
                else:
                    flag = 0
                    while(end < len(str)):
                        if str[end] >= '0' and str[end] <= '9':
                            end += 1
                        else:
                            break
                    start += 1 # 
                    if start == end:
                        return 0
                break
            elif c == ' ':  # 空格继续往后找
                continue
            else:  # 其他字符任务失败
                return 0  
        # 转换成整形
        num = int(str[start:end])
        # 给符号
        if flag:
            pass
        else:
            num = -num
            
        if num >= -2147483648 and num <= 2147483647:
            return num
        elif num < -2147483648:
            return -2147483648
        else:
            return 2147483647