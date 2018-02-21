class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 把事情做完，盯着'('就可以了
        # 用贪心算法，cmax记录最大未匹配'('数目
        # cmin记录必须匹配的'('数目，也即最小未匹配数目
        # 贪心规则：cmax必须大于等于0，小于就完了，意味着')'过多
        # cmin如果为0，则返回True，这也意味着存在一种组合使得'('都被匹配
        cmax = cmin = 0
        for c in s:
            if c == '(':
                cmax += 1
                cmin += 1
            elif c == ')':
                cmax -= 1
                cmin = max(cmin-1, 0)
            elif c == '*':
                cmax += 1
                cmin = max(cmin-1, 0)
            if cmax < 0:
                return False
        return cmin == 0