# 法1：模拟游戏过程编程，超时
class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 创建一个list
        nums = []
        for i in range(1, n+1):
            nums.append(i)    
        
        # 初始化删除的下标
        flag = 1  # 0是偶数行 1是奇数行
        index = 0
        
        while len(nums) > 1:
            if flag:
                nums.pop(0)
                index = 1
                while index < len(nums):
                    nums.pop(index)
                    index += 1
                flag = 0
                
            else:
                print(nums)
                nums.pop(len(nums)-1)
                index = len(nums) - 2
                while index >= 0:
                    print(nums)
                    nums.pop(index)
                    index -= 2
                flag = 1
            
        
        
        return nums[0]
    
# 法2：快速算法，只观察头指针，最后剩余的一个数就是结果
class Solution:
    def lastRemaining(self, n):
        # 只盯着头指针看，最后剩的唯一元素就是目标
        head = step = 1
        # 剩余多少个数？
        remaining = n
        # 判断是从左往右删还是从右往左删
        # 从左往右删一定是要移动头指针的，但从右往左删不一定
        # 从右往左删需要判断
        left2right = True
        while remaining > 1:
            if left2right or remaining % 2 == 1:
                head += step
            remaining //= 2
            step *= 2  
            # 从左往右和从右往左交替进行
            left2right = not left2right
            
        return head