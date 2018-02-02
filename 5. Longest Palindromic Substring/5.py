# 思路1：超时了
class Solution:
    def longestPalindrome(self, s):
        substring = ""
        if len(s) == 1:
            return s
        max_length = length = start = 0
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1-max_length):
                length = i - j + 1
                if length > max_length and self.isPalindromicSubstring(s[j:i+1]):
                    print(i,j)
                    substring = s[j:i+1]
                    max_length = length
                    break
            # 判断，如果下一个时刻的搜索范围已经不可能超过max_length，则结束
            if i <= max_length:
                return substring
        return substring
        
    def isPalindromicSubstring(self, s):
        i = 0
        j = len(s)-1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True



# 思路2： 双指针，以一个回文的中心元素作为查找依据，省去很多时间
# 也即假设s[i]是回文的中心=》自然想到分奇偶讨论
class Solution:
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s
        max_length = 0
        l = len(s)
        # 找中心点 分奇偶讨论
        for i in range(l):
            # 如果剩余长度的一半都不到最大长度，那么对于这个i可以直接过掉
            # 节省几乎一半的时间
            if min(l-i, i+1) < max_length/2:
                break
            # 1.假设s[i]是奇数回文中心
            k1 = k2 = i
            while k1 >= 0 and k2 < l:
                if s[k1] == s[k2]: 
                    k1 -= 1  # 注意，还多减了一个，最后要加回来
                    k2 += 1
                else:
                    break
            if max_length < k2 - k1 - 1:
                max_length = k2 - k1 - 1
                start = k1 + 1   # 能不用字符串赋值就尽量不用，又省三分之一时间
                end = k2
            # 2.假设s[i]是偶数回文中心
            k1 = i
            k2 = i + 1
            while k1 >= 0 and k2 < l:
                if s[k1] == s[k2]:
                    k1 -= 1
                    k2 += 1
                else:
                    break
            if max_length < k2 - k1 - 1:
                max_length = k2 - k1 - 1
                start = k1 + 1
                end = k2
        return s[start:end]