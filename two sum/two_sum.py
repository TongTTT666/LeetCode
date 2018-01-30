class Solution:
    def twoSum(self, nums, target):
        # 判断长度，如果数组长度不到2，则不可能完成目标
        if len(nums) < 2:
            return False
        # 构建一个字典，该字典的任务就是存储 需要数字：数字下标的对应关系
        # 也即7:2 说明7这个数字是nums中下标为2的数字所需要的
        dict_need = {}
        # 过一遍
        for index, num in enumerate(nums):
            # 如果该数字在字典中存在(key)，则说明target可以完成，那么也就返回
            # 对应的index和dict_need[num]，也即key所对应的value值
            # 否则，就说明该数字不是当前所需要的，在字典中记录下这个数字所需要的数字
            if num in dict_need:
                return [dict_need[num], index]
            else:
                dict_need[target - num] = index