class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # 不能简单的直接套用算法作业的那一题，因为两个数组的长度不一样
        # 需要讨论的情况太多
        # 最关键思路的一句话：中位数就是找到某个数，使得能够将一组数分成两个部分，
        # 其中一个部分的数总是比另外一部分小
        # 将nums1定为长度小的那个，可以节省二分搜索时间
        m = len(nums1)
        n = len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        if n == 0:   # 只有一个数，有一个数组是空的
            return nums1[0]
        
        # 确定初始搜索区间，用二分查找 这里对于奇数的一半长度采用+1策略，也即m+n=5，则half_length=3
        imin, imax, half_length = 0, m, (m+n+1) // 2
        # 该算法的目标：就是找到一个i以及其对应的j，是的i+j包含一半的元素，
        # 并且要求nums1[i-1] < nums2[j] and nums1[j-1] < nums2[i]
        # 对退少补，类似算法那个题，也是二分查找，才能实现O(logn)的复杂度
        while True:
            # 确定当前二分点，这个不重要，只要保证i+j=half_length即可
            i = (imin + imax)//2
            j = half_length - i
            # 判断第一种情况，如果nums1[i-1]>nums2[j]，则i的取值太大，要减少i
            # 但必须确保，i的值不能减到负数，最小是0，否则就非法了
            if i > 0 and nums1[i-1] > nums2[j]: # 注意两个字句的先后顺序，有很大影响 
                imax = i - 1   # 二分，直接缩小一半的搜索空间，因为下一轮的i肯定在0到i-1取     
            # 第二种情况，如果nums1[j-1]>nums2[i]，说明i的取值太小了，要增加i
            # 但必须保证，i要合法，也即i<m，否则就是非法了
            elif i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            # 最后一种情况，找到了合适的i，满足上述条件
            else:
                # 讨论特殊情况，也就是i=0或j=m的情况，先求左边最大值
                if i==0:
                    left_max = nums2[j-1]
                elif j==0:
                    left_max = nums1[i-1]
                else: # 正常情况
                    left_max = max(nums2[j-1],nums1[i-1])
                
                # 先算最大值，因为奇数数情形根本都不用算，可以节省时间
                if (m+n) % 2 == 1:
                    return left_max
                
                # 再求最小值，只有偶数情形需要
                if i == m:
                    right_min = nums2[j]
                elif j == n:
                    right_min = nums1[i]
                else:
                    right_min = min(nums2[j], nums1[i])
                
                return (left_max+right_min)/2
                