# 法1：时间183ms
class Solution:
    def convert(self, s, numRows):
        # 给你一个zigzag让你转换成另外一种表达
        # 其实就是一个找规律的题，
        convert_s = [''] * len(s)
        new_index = index = 0  # 一个是新索引，一个是旧索引
        if numRows==1:
            return s
        for i in range(numRows):
            if i == 0: # 第一行
                index = 0
                while index <= len(s) - 1: # 不能超过字符串的最大索引
                    convert_s[new_index] = s[index]
                    new_index += 1
                    index += 2*numRows-2
            elif i > 0 and i < numRows-1:  # 中间的所有行
                index = i
                flag = 0 # 因为是两个一组的
                offset = [2*numRows-2-i*2, i*2]
                while index <= len(s)-1:
                    convert_s[new_index] = s[index]
                    new_index += 1
                    index += offset[flag]
                    if flag:
                        flag = 0
                    else:
                        flag = 1
            else: # 最后一行
                index = numRows - 1
                while index <= len(s) - 1: # 不能超过字符串的最大索引
                    convert_s[new_index] = s[index]
                    new_index += 1
                    index += 2*numRows-2
        convert_s = ''.join(convert_s[0:new_index])
        return convert_s

# 法2:175ms
class Solution:
    def convert(self, s, numRows):
        # 给你一个zigzag让你转换成另外一种表达
        # 其实就是一个找规律的题，
        convert_s = ""
        index = 0  # 一个是新索引，一个是旧索引
        if numRows==1:
            return s
        for i in range(numRows):
            if i == 0: # 第一行
                index = 0
                while index <= len(s) - 1: # 不能超过字符串的最大索引
                    convert_s += s[index]
                    index += 2*numRows-2
            elif i > 0 and i < numRows-1:  # 中间的所有行
                index = i
                flag = 0 # 因为是两个一组的
                offset = [2*numRows-2-i*2, i*2]
                while index <= len(s)-1:
                    convert_s += s[index]
                    index += offset[flag]
                    if flag:
                        flag = 0
                    else:
                        flag = 1
            else: # 最后一行
                index = numRows - 1
                while index <= len(s) - 1: # 不能超过字符串的最大索引
                    convert_s += s[index]
                    index += 2*numRows-2
        return convert_s