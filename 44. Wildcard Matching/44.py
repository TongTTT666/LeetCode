class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 2D Dynamic Programming
        
        # Initial DP
        # dp[i][j] means that whether p[0...j) can match s[0...i)
        # dp[0][0] = True because empty string can match empty string
        # the result is dp[len(s)][len(p)]
        dp = [[False for x in range(len(p)+1)] for y in range(len(s)+1)] 
        
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = True
            else:
                break
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                # divide into two situations
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')     
                else:
                    # '*' can be considered as empty string or any nonempty string
                    dp[i][j] = dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j]
                    
        return dp[len(s)][len(p)]
                    
                    
                    