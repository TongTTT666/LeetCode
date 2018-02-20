class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 定一点双指针调整
        # 定一点i，双指针left和right，一共三个数字，i定死，left只能右移，right只能左移
        # 满足上面要求我们需要把数字按升序排列才可以
        nums.sort()
        res = []
        # 不符合题目要求的滚蛋
        if len(nums) < 3:
            return res
        # 遍历开始数，也即三个数的头一个数，最小的数
        for i in range(len(nums)-2):
            left, right = i + 1, len(nums)-1  # 左右指针
            # 相同的开始数，只做一次
            # 第一个数必须求，否则遇到类似[0,0,0]返回的就是空集了
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                if _sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # 去掉重复的数
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif _sum < 0: # 和小了，增加数字大小，左边指针右移
                    left += 1
                else:
                    right -= 1 # 和大了，减少数字大小，右边指针左移
        return res    