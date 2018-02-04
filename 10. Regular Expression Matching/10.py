# 法1：114 ms
class Solution:
    def isMatch(self, s, p):
        # DP算法解决匹配问题，难度较大
        # 创建初始情况 dp[i][j]=True表示p[0...j)可以表示s[0...i)
        m = len(s)
        n = len(p)
        dp = [[False for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = True  # 初始化为True，目标是看True能否传递到dp[m][n]
        # 对第一行初始化
        for j in range(1, n + 1):
            dp[0][j] = p[j - 1] == '*' and dp[0][j - 2]

        # 开始动态规划过程
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1]
                                                     or p[j - 1] == '.')
                else:
                    dp[i][j] = dp[i][j - 2] or dp[i - 1][j] and (
                        s[i - 1] == p[j - 2] or p[j - 2] == '.')

        return dp[m][n]
