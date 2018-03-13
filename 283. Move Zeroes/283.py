class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
    
        # Define two pointer, one links to zero and the other links to nonzero
        p0, p1 = 0, 0
    
        while True:
            # we must make it in this order:
            # find a zero, then find a nonzero number, finally exchange them
            # p0 pointer must be zero!!
            while p0 < len(nums) and nums[p0]:
                p0 += 1
            # p1 pointer can not be zero!! p1 must behind p0, since we need move all 0's to the end
            while p1 < len(nums) and not nums[p1] or p1 <= p0:
                p1 += 1
                
            # exchange 
            if p1 < len(nums) and p0 < len(nums):
                nums[p0], nums[p1] = nums[p1], nums[p0]
            else:
                return
            
            
            
            
            