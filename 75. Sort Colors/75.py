# 法1：记录每个颜色的数目，然后覆盖原数组
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        t = [0, 0, 0]
        for i in range(len(nums)):
            t[nums[i]] += 1
        print(t)
        index = 0
        while index < len(nums):
            if t[0] > 0:
                nums[index] = 0
                t[0] -= 1
            elif t[1] > 0:
                nums[index] = 1
                t[1] -= 1
            elif t[2] > 0:
                nums[index] = 2
                t[2] -= 1
            index += 1

# 法2： one-pass方法
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # one-pass 方法
        # 定头尾指针 p1 p2 以及遍历下标index
        # 最后p1及其前面的数一定是0，p2及其后面的数一定是2
        p1, p2, index = 0, len(nums)-1, 0
        while index <= p2:
            if nums[index] == 0:
                nums[index], nums[p1] = nums[p1], 0
                p1 += 1
                # 这个地方拿到前面的数一定是0，根本不需要讨论
            if nums[index] == 2:
                nums[index], nums[p2] = nums[p2], 2
                p2 -= 1
                # 因为你从后面换回来的数，不确定
                index -= 1
            index += 1
            
            
        
                
            
        
      