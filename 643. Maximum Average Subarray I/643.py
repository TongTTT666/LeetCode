class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # use sliding-window, so easy
        totle, maxTotle = 0, -10000
        # calculate a initial sum, when we slide the window,
        # the only thing we should do is add the next number and sub the last number
        # Now, we assume the result is the sum of first k numbers
        maxTotle = totle = sum(nums[:k])
        
        for i in range(1, len(nums)-k+1):
            totle += (-nums[i-1] + nums[i+k-1])
            if totle > maxTotle:
                maxTotle = totle
        
        return maxTotle / k