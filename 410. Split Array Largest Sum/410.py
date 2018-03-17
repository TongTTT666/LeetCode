class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # binary search for RANGE
        # Assume mid is the solution and validate mid is larger? smaller? than the real solution
        # Then, adjust the range until left = right -> left is just the result
        
        # Strategy: mid is the solution, which means that we can divide this array into m subarrays, 
        # and the min-max sum is just mid. However, sometimes we can not make it. -> If we have m subarrays,
        # we can not ensure that the sum of every subarray is equal or less than mid. So, we attempt to
        # divide the input array and make every subarray's sum is equal or less than mid. Finally, we
        # calculate how many subarrays we have divided. If the number of subarrays is more than m, mid is too small.
        # If the number of subarrays is less than m, mid is too large.
        
        # Initial left and right
        left, right = max(nums), sum(nums)
        
        def canDivideMoreThanmSubarray(mid, nums, m):
            cut = _sum = 0
            for num in nums:
                _sum += num
                if _sum > mid:
                    cut += 1
                    _sum = num
                    # m-1 cuts = m subarrays
                    if cut > m-1:
                        return True
            return False
        
        while left < right:
            mid = (left + right) // 2
            if canDivideMoreThanmSubarray(mid, nums, m):
                left = mid + 1
            else:
                right = mid
                
        return left
    
        
            
            
            
            
            
            