class Solution:
    def lengthOfLongestSubstring(self, s):
        # 很典型的动态规划问题
        N = len(s) # 字符串长度
        if N == 0: # 排除空字符串情形
            return 0
        #dp = [0 for i in range(N)]  # 是否能不创建数组？
        #dp[0] = 1
        dp = 1
        pre = 0 # 确定下一次从哪个位置开始检索
        for i in range(1, N):
            if s[i] in s[pre:i]:
                pre = s.index(s[i], pre, i) + 1  
                length = i - pre + 1  # 计算当前分析字符串的长度 一旦出现重复的，就需要截取后面一部分单独分析
                #dp[i] = max(length, dp[i-1])
                dp = max(length, dp)
            else:
                length = i - pre + 1 
                #dp[i] = max(length, dp[i-1])
                dp = max(length, dp)        
        #return dp[N-1]
        return dp