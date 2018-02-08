import math
class Solution:
    def constructRectangle(self, area):
        W = int(math.sqrt(area))
        # 直接把W往下寻找
        while area % W != 0:
            W -= 1
        return [area//W, W]
        