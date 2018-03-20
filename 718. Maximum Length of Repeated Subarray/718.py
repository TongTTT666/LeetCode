class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # DP algorithm
        # dp[i][j]: the maximum length of an subarray that appears in A[i:] and B[j:].
        # we can find that dp[i][j] = dp[i+1][j+1] + 1 if A[i] == B[j]
        
        dp = [[0] * (len(B)+1) for x in range(len(A)+1)]
        
        for i in range(len(A)-1, -1, -1):
            for j in range(len(B)-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                
      
        return max(max(row) for row in dp)

# 把上述方案修改一下，也是对的
class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # DP algorithm
        # dp[i][j]: the maximum length of an subarray that appears in A[i:] and B[j:].
        # we can find that dp[i][j] = dp[i-1][j-1] + 1 if A[i-1] == B[j-1]
        
        dp = [[0] * (len(B)+1) for x in range(len(A)+1)]
        
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
       
        return max(max(row) for row in dp)