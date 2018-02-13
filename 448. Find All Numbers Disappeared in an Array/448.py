class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res, dis = [False]*len(nums), [] # 弄个数组记录每个数字是否出现
        for i in range(len(nums)):
            # 数字出现了，就把该值变为True
            res[nums[i]-1] = True
        # 找到那些False对应的i，i+1就是最后的结果
        for i in range(len(nums)):
            if res[i] == False:
                dis.append(i+1)
        
        return dis