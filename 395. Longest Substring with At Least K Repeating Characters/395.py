# 法1：Divide and Conquer 超时了，还需要修改
class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # 思路：以出现频率低于k的字符作为分割点
        if len(s) < k:
            return 0
        
        # 统计每个字母出现的频率，用字典Counter
        fre = collections.Counter()
        for i in range(len(s)):
            fre[s[i]] += 1
        
        # 最少的重复次数都大于等于要求了，自然返回整字符串长度
        if min(fre.values()) >= k:
            return len(s)
        
        cur = 0
    
        # 然后以那些没有达到次数的作为分隔符，递归调用函数计算子字符串的长度
        # 一个当前cur指针往下指，专门找次数不够的
        while cur < len(s):
            if fre[s[cur]] < k:
                left = self.longestSubstring(s[:cur], k)
                right = self.longestSubstring(s[cur+1:], k)
                return max(left, right)
            else:
                cur += 1
        

# 法2：要进一步加速，这种策略就通过了，但还是非常慢
class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # 思路：以出现频率低于k的字符作为分割点
        if len(s) < k:
            return 0
        
        # 统计每个字母出现的频率，用字典Counter
        fre = collections.Counter()
        for i in range(len(s)):
            fre[s[i]] += 1
        
        # 最少的重复次数都大于等于要求了，自然返回整字符串长度
        if min(fre.values()) >= k:
            return len(s)
        
        cur = 0
    
        # 然后以那些没有达到次数的作为分隔符，递归调用函数计算子字符串的长度
        # 一个当前cur指针往下指，专门找次数不够的
        for c in fre:
            if fre[c] < k:
                for i in range(len(s)):
                    if s[i] == c:
                        left = self.longestSubstring(s[:i], k)
                        right = self.longestSubstring(s[i+1:], k)
                        return max(left, right)

# 法3：利用python中的set提取字符串s中出现的每个字符（不重复），再用count函数统计set中没有元素
# 在s中的出现次数，这个速度就非常快了，快乐10多倍，时间主要节省在字典的创建
class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # 思路：以出现频率低于k的字符作为分割点
        if len(s) < k:
            return 0
    
        # 然后以那些没有达到次数的作为分隔符，递归调用函数计算子字符串的长度
        # 一个当前cur指针往下指，专门找次数不够的
        for c in set(s):
            if s.count(c) < k:
                for i in range(len(s)):
                    if s[i] == c:
                        left = self.longestSubstring(s[:i], k)
                        right = self.longestSubstring(s[i+1:], k)
                        return max(left, right)
        
        
        return len(s)