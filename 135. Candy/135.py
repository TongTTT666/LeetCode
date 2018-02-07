class Solution:
    def candy(self, ratings):
        # 这个题目要分左右来看，用两个数组更加容易理解
        # 先搞定左->右的关系，越大我越加，不大我清1
        # 再搞定右->左的关系，越大我越加，不大我清1
        # 最后来一个取最大值，就可以保证两个要求都满足
        # 上述就是贪心规则，也是贪心算法中最重要的一步！

        # 创建两个list
        left2right, right2left, result = [], [], []
        num1 = num2 = 1  # 记录连续生长的个数
        left2right.append(1)
        right2left.append(1)
        re_ratings = ratings[::-1]  #反转

        for i in range(1, len(ratings)):
            if ratings[i - 1] >= ratings[i]:
                left2right.append(1)
                num1 = 1
            else:
                left2right.append(1 + num1)
                num1 += 1

            if re_ratings[i - 1] >= re_ratings[i]:
                right2left.append(1)
                num2 = 1
            else:
                right2left.append(1 + num2)
                num2 += 1

        right2left.reverse()
        # 取大的那个
        for i in range(len(ratings)):
            if left2right[i] >= right2left[i]:
                result.append(left2right[i])
            else:
                result.append(right2left[i])

        return sum(result)