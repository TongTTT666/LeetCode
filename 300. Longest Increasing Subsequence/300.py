class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 用tails[i]表示长度为i+1的所有连续增长子字序列末尾元素最小值
        tails = [0 for i in range(len(nums))]
        # 初始长度设为0
        size = 0
        # 接下来用二分法查找即可，对于每一个nums中的数字，用二分法
        # 在tails查找其大概的位置，可能能够查到，也可能会覆盖某个值
        # 也可能根本查不到是一个新的值，如果这个值是一个大值，那么
        # 就会增加增长子序列的长度，因为后面出现了大值
        for x in nums:
            # 两个查找指针，一头一尾，size记录最长增长子序列
            i,j = 0, size
            while i < j:    # 停止条件
                mid = (i + j) // 2
                if tails[mid] < x:
                    i = mid + 1
                else:
                    j = mid
            tails[i] = x
            
            if i == size:  # 遇到大值了
                size += 1
                
        return size