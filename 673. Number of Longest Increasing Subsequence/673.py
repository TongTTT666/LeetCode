class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 一道典型的动态规划问题
        # 动态规划变量dp[i]
        # 含义是以第i个字符结尾的最长字符递增子序列的长度
        # 此时还需要一个对应的数组变量(count)
        # count记录以nums[i]为结尾的最长字符串有几种形式
        # 最后取最长长度值所对应的那个数即可
        if not nums:
            return 0
        
        # 初始化
        dp = [1] * len(nums)
        # 初始化全为1，至少有一种形式
        count = [1] * len(nums)
        # O(n^2)的时间
        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    if dp[j]+1 > dp[i]:
                        # 出现了一种更长的情况！！！！
                        # 更新动态规划变量
                        dp[i] = dp[j] + 1
                        # 也即顺着nums[j]过来，如果count[j]是2种
                        # 那么此时count[i]也应该有两种
                        count[i] = count[j]
                    elif dp[j]+1 == dp[i]:
                        # 如果出现了重复最长的情况！那么就把对应的count加上
                        count[i] += count[j] 
                    
        max_length = max(dp)
        _sum = 0
        # 提出count中最大的长度所对应的数字并求和
        for i in range(len(nums)):
            if dp[i] == max_length:
                _sum += count[i]
            
            
            
        return _sum
                    
                    
        
                
        