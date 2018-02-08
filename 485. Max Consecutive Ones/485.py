class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # 动态规划可以，直接找0也可以O(n)
        last = current = -1  # 要默认是0的前面那个是0
        length = max_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                current = i
                # 计算间隔
                length = current - last - 1
                if length > max_length:
                    max_length = length
                last = current
            
        # 不排除末尾有可能不是以0结尾的可能，还要单独算一个结尾
        if current != len(nums) - 1:
            length = len(nums) - current - 1
            if length > max_length:
                max_length = length
        
        return max_length