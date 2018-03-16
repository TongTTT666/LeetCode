class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Dynamic Programming problem?!
        # What is the DP variable?
        # depth? dp[i] -> i indicate depth?
        # Before solving this problem, I should learn what is BST.
        # Two conditions of BST=> 1、左节点及以下节点的值比它小；2、右节点及以下节点的值比它大
        # Based on these two conditions, we can use DP to solve it.
        # choose one number i as root, divide these numbers into two subsequence [1,2,...i-1], [i+1,...,n]
        # Now, we can obtain two subproblem: use number [1,2,...i-1] and [i+1,...,n] to 
        # establish two BSTs => recursion problem => DP problem
        
        # Define two functions: 
        # dp[i]: the number of unique BST for a sequence of length n
        # F[i][n]: the number of unique BST for a sequence of length n where number i is the root of BST 
        # We can find a connection between dp and F, dp[n] = F[1][n] + F[2][n] + ... + F[n][n], that is trivial
        # For anyone of F[i][n], we have F[i][n] = dp[i-1] * dp[n-i] since we can divide these numbers
        # into two subsequence  [1,2,...i-1], [i+1,...,n] and use them to establish two sub-BSFs
        # => actually there are dp[i-1]*dp[n-i] ways to make it => recursion problem
        # Thus, dp[n] = dp[0]*dp[n-1] + dp[1]*dp[n-2] + ... dp[n-1]*dp[0]
        # Initializaion: dp[0] = 1 and dp[1] = 1 => trivial
        # If we want to obtain the value of dp[3], we must need dp[0], dp[1] and dp[2] => that is DP algorithm!!!
        
        #dp = [0 for i in range(n+1)]
        #dp[0] = dp[1] = 1
        dp = [1, 1] + [0] * (n-1)
        
        for i in range(2, n+1):
            for j in range(n):
                dp[i] += dp[j] * dp[i-j-1]
                
        return dp[n]
        
        
        
        
        