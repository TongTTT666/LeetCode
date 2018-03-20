class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # two pointer problem
        p1, p2, Sum, minLength = 0, 0, 0, len(nums)+1
        
       
        while p2 < len(nums):
            Sum += nums[p2] 
            while Sum >= s:
                Sum -= nums[p1]
                minLength = min(minLength, p2-p1+1)
                p1 += 1
            p2 += 1
            
            
            
        if minLength > len(nums):
            # there isn't one
            return 0
        else:
            return minLength