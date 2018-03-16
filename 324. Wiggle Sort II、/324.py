class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # sort nums
        nums.sort()
    
        # get the length of half numbers
        half = len(nums[::2])
        
        # put larger numbers to the odd position and put smaller numbers to the even position
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        