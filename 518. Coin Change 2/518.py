# 法1：基本动态规划 速度较慢 通过
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # 尝试用动态规划求解
        # 建立动态规划变量，几维？需要明确
        # 本题也是两维，第一维是最多使用的钱币种类数目，第二维是搞定的金额
        # 那么返回的就是dp[len(coins)][amount]，第一行包括空硬币的情形
        # 需要排除硬币为空的情况，要加入一列
        # 声明dp dp[i][j]表示用前i个硬币组合成j块钱的组合方法 dp[0][j]表示前0个硬币，也即不用硬币表示j块钱
        # i的取值范围0到len(coins) j的取值范围为0到amount
        dp = [[0 for x in range(amount + 1)] for y in range(len(coins) + 1)]
        # 不用硬币只能表示1块钱
        dp[0][0] = 1
        # 前i个硬币表示0块钱肯定有一种表示方法
        for i in range(1, len(coins) + 1):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                # dp[i][j]的数目等于dp[i-1][j]加上dp[i][j-coins[i]]如果j-coins[i]>=0
                # 第一项代表少一枚硬币表示同样数目钱的种类数目，也即不用第i种硬币，第二项表示用第i种硬币
                # 并且能够满足amount需求的，也即j必须大于等于当前种类硬币的价值，否则钱大目标少是不可能实现的
                if j >= coins[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[len(coins)][amount]


# 法2：优化动态规划，速度较快，二维减为一维
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # 尝试用动态规划求解
        # 这次尝试将二维变成一维
        # 是通过观察发现实际的动态规划过程与i无关才决定化简的
        # 简化2维的思路，原理是从2维来的
        dp = [0] * (amount + 1)
        # 不用硬币只能表示1块钱
        dp[0] = 1
        # 前i个硬币表示0块钱肯定有一种表示方法
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if j >= coins[i]:
                    dp[j] += dp[j - coins[i]]

        return dp[amount]