class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # use binary search for range not for index !!!
        
      
        # sort the original array
        nums.sort()
        
        # define basic elements
        low, high = 0, nums[-1] - nums[0]
        
        # define a counter
        cnt = 0    
        
        # set one number and move another pointer to count how many distances less or equal to mid
        # That means we set one number as head and adjust the other number as tail
        while low < high:
            cnt = 0
            mid = (low + high) // 2
            # Initial j !!!
            j = 0
            for i in range(len(nums)):
                while j < len(nums) and nums[j]-nums[i] <= mid:
                    j += 1
                # count how many pairs' distance less or equal to mid when nums[i] is the first element 
                # add to the counter
                cnt += j-i-1

            # binary search -> adjust high or low
            if cnt < k:
                low = mid + 1
            else:
                high = mid
        
        
        return low
            
            
            
            
            