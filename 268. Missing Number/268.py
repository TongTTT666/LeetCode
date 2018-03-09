class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0] * (len(nums)+1)
        
        for number in nums:
            count[number] += 1
            
        for i in range(len(nums)+1):
            if count[i] == 0:
                return i
        
        