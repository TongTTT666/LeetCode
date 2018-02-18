class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        
        # 最大交易次数
        num = 2
        # 动态规划表示变量dp[k][day]表示第day天至多k次交易的最大收入
        dp = [[0 for i in range(len(prices))] for j in range(num+1)]
        
        for k in range(1, num+1):
            temp = dp[k-1][0] - prices[0] # 假设第0天借钱买股票
            for day in range(1, len(prices)):
                # 问题是第0天买划算吗？那就试试看第day天卖出划不划算
                # 其实不一定第一天买，这步就是判断第day天卖的收益怎么样
                dp[k][day] = max(dp[k][day-1], prices[day] + temp)
                # 更新temp，假设在第day天买，也即不一定第0天买，相比前一天来说又多花钱了
                temp = max(temp, dp[k-1][day] - prices[day])
                
        return dp[num][len(prices)-1]