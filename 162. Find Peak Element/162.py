class Solution(object):
    def findPeakElement(self, nums):
        # 用二分查找去查
        # left 和 right是查找范围
        if len(nums) <= 1:
            return 0
        
        left, right = 0, len(nums)-1
        while left >= 0 and right < len(nums):
            mid = (right + left) // 2      
            
            if mid == len(nums)-1:
                if nums[mid] > nums[mid-1]:
                    return mid
                else:
                    return mid-1
            elif mid == 0:
                if nums[mid] > nums[mid+1]:
                    return mid
                else:
                    return mid+1
            
            if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                return mid
            elif nums[mid-1] >= nums[mid+1]:
                right = mid - 1
            elif nums[mid-1] < nums[mid+1]:
                left = mid + 1