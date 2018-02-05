class Solution:
    def monotoneIncreasingDigits(self, N):
        # 贪心 greedy
        # 数字的位数
        digit = len(str(N))
        temp = 0
        flag = 0  # 记录如果出现了前两位相等，后一位比上一位小，也即不能减一
        while digit > 1:
            # 先从高位开始提，提相邻两位进行比较
            d1 = N // 10**(digit-1) % 10  # 提第一位
            d2 = N // 10**(digit-2) % 10  # 提第二位
            if d1 > d2: # 不符合情况 第一位减掉1 后面所有位全变成9，直接返回
                if not flag:
                    d1 -= 1 
                    temp += d1 * 10 ** (digit-1)
                    digit -= 1
                    while digit > 0:
                        temp += 9 * 10 ** (digit-1)
                        digit -= 1
                    return temp
                else: #  从相等的第一位减一，后面直到最后一位全部给我变为9
                    digit = eq_digit
                    temp -= 1 * 10 ** (digit-1)
                    temp -= temp % 10 ** (digit-1)
                    digit -= 1
                    while digit > 0:
                        temp += 9 * 10 ** (digit-1)
                        digit -= 1
                    return temp
            elif d1 == d2:  # 出现等于情况，记录一下（包括flag和刚开始相等的第一位），但还是照常做
                if not flag:
                    flag = 1
                    eq_digit = digit
                temp += d1 * 10 ** (digit-1)
            else:  # 正常情况不动
                temp += d1 * 10 ** (digit-1)
                flag = 0
            digit -= 1
            
        # 返回的时候要加上最后一位
        return temp + d2