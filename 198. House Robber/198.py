class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        # 设定动态规划变量dp
        # dp[i]含义：计划抢到第i个房子的最大收益，最后返回dp[len(nums)-1]即可
        # 初始化：收益为0，因为i必须从2开始，所以我们必须把前两天的收益写出来
        dp = [0] * len(nums)
        dp[0] = nums[0] # 计划抢到第0个房子，肯定是抢收入高
        dp[1] = max(nums[0], nums[1]) # 计划抢到第1个房子，我可以抢0也可以抢1，但不能同时抢，谁大抢谁
        for i in range(2, len(nums)):
            # 是否抢第i个房子，前面一项是不抢第i个房子，后面一项是抢第i个房子，看谁收益大
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        
      
        return dp[len(nums)-1]
        