# 法1：二分法很慢
class Solution:
    def mySqrt(self, x):
        # 用二分查找吧，也许可以快一点
        # left和right分别是搜索的左右区间，闭区间
        left, right = 0, x
        while True:
            mid = (left + right) // 2
            if mid**2 == x:
                return mid
            elif (mid + 1)**2 == x:
                return mid + 1
            elif mid**2 < x and (mid + 1)**2 > x:
                return mid
            elif (mid + 1)**2 < x:  # 要往大的那一半搜
                left = mid + 1
            elif mid**2 > x:
                right = mid


# 法2：随机法，比方法1还要慢
import random
class Solution:
    def mySqrt(self, x):
        # 用随机分点查找吧，也许可以快一点
        # left和right分别是搜索的左右区间，闭区间
        left, right = 0, x
        while True:
            mid = random.randint(left, right)
            if mid**2 == x:
                return mid
            elif (mid + 1)**2 == x:
                return mid + 1
            elif mid**2 < x and (mid + 1)**2 > x:
                return mid
            elif (mid + 1)**2 < x:  # 要往大的那一半搜
                left = mid + 1
            elif mid**2 > x:
                right = mid

# 法3：随机更改法去掉初始一半的搜索区间以增加速度，还是很慢
import random
class Solution:
    def mySqrt(self, x):
        # 用随机分点查找吧，也许可以快一点
        # left和right分别是搜索的左右区间，闭区间
        if x == 0 or x == 1:
            return x
        left, right = 0, x//2
        while True:
            mid = random.randint(left, right)
            if mid**2 == x:
                return mid
            elif (mid+1)**2 == x:
                return mid+1
            elif mid**2 < x and (mid+1)**2 > x:
                return mid
            elif (mid+1) ** 2 < x:  # 要往大的那一半搜
                left = mid + 1
            elif mid ** 2 > x:
                right = mid

# 法4：二分法去掉初始一半搜索区间，又快了一些
class Solution:
    def mySqrt(self, x):
        # 用二分查找吧，也许可以快一点
        # left和right分别是搜索的左右区间，闭区间
        if x == 0 or x == 1:
            return x
        left, right = 0, x//2   # 初始去掉一般搜索空间以增加速度
        while True:
            mid = (left + right) // 2
            if mid**2 == x:
                return mid
            elif (mid + 1)**2 == x:
                return mid + 1
            elif mid**2 < x and (mid + 1)**2 > x:
                return mid
            elif (mid + 1)**2 < x:  # 要往大的那一半搜
                left = mid + 1
            elif mid**2 > x:
                right = mid
                
# 法5：二分法更改if语句的判断顺序，提升了很大的速度
class Solution:
    def mySqrt(self, x):
        # 用二分查找吧，也许可以快一点
        # left和right分别是搜索的左右区间，闭区间
        if x == 0 or x == 1:
            return x
        left, right = 0, x//2   # 初始去掉一般搜索空间以增加速度
        while True:
            mid = (left + right) // 2
            if (mid + 1)**2 < x:  # 要往大的那一半搜
                left = mid + 1
            elif mid**2 > x:
                right = mid
            elif mid**2 == x:
                return mid
            elif (mid + 1)**2 == x:
                return mid + 1
            elif mid**2 < x and (mid + 1)**2 > x:
                return mid

# 法6：去掉一些特殊情况，会稍微增加速度
class Solution:
    def mySqrt(self, x):
        # 用二分查找吧，也许可以快一点
        # left和right分别是搜索的左右区间，闭区间
        # 特殊情况拿出来以缩小初始范围
        if x == 0 or x == 1:
            return x
        elif x <= 3 and x >= 2:
            return 1
        elif x > 3 and x <= 8:
            return 2
        elif x > 8 and x <= 15:
            return 3
        
        left, right = 4, x//4   # 初始去掉一般搜索空间以增加速度
        while True:
            mid = (left + right) // 2
            if (mid + 1)**2 < x:  # 要往大的那一半搜
                left = mid + 1
            elif mid**2 > x:
                right = mid
            elif mid**2 == x:
                return mid
            elif (mid + 1)**2 == x:
                return mid + 1
            else:
                return mid
