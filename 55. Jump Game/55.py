# 这是自己编写的思路
# 分析每一个0的位置，遍历0位置前面的所有元素
# 只要存在一个能把这个0跨过去就说明没问题
# 否则就说明这个路走不通
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 关键问题就是判断0的位置是不是死路一条，其他无所谓
        flag = False
        for i in range(len(nums)):
            if i == len(nums)-1:
                return True
            if not nums[i]:  # 看你能不能过一个坎
                flag = False
                for j in range(i):
                    if nums[j] > i - j:
                        flag = True 
                        break
                if not flag:  # 如果不能过这个坎，就完了  
                    return False
                
        return True

# 以下是借鉴大神的方法
# 每个节点分析，当前最大能到达的位置与该节点的位置逐一比较
# 如果该节点的位置已经大于最大到达位置，就说明任务失败
# 还不如我的快
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        can_reach = 0
        for i in range(len(nums)):
            if i > can_reach:
                return False
            can_reach = max(can_reach, i+nums[i])
        return True

