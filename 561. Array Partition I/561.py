class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # just sort this numbers and calculate the sum of even index's numbers 
        nums.sort()
        i = Sum = 0
        while i < len(nums):
            Sum += nums[i]
            i += 2
            
        return Sum
            