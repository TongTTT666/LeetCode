# 简化前，更清晰
class Solution:
    def isIsomorphic(self, s, t):
        # Hash Table的一个实例，用字典去解决对应关系的问题
        hashTable = {} # 声明字典
        # 先构建哈希表，然后再查，我觉得肯定是慢的
        for i in range(len(s)):
            if s[i] not in hashTable:
                hashTable[s[i]] = t[i]
        
        for i in range(len(t)):
            if hashTable[s[i]] != t[i]:
                return False
        
        # 把s和t反过来再做一次，要防止出现重复元素对应的情况
        s, t = t, s
        hashTable = {} # 声明字典
            
        for i in range(len(s)):
            if s[i] not in hashTable:
                hashTable[s[i]] = t[i]
        
        for i in range(len(t)):
            if hashTable[s[i]] != t[i]:
                return False
            
        return True
        
# 简化后，速度更快
class Solution:
    def isIsomorphic(self, s, t):
        # Hash Table的一个实例，用字典去解决对应关系的问题
        hashTable = {} # 声明字典
        # 先构建哈希表，然后再查，我觉得肯定是慢的
        for i in range(len(s)):
            if s[i] not in hashTable:
                hashTable[s[i]] = t[i]
            if hashTable[s[i]] != t[i]:
                return False
        
        # 把s和t反过来再做一次，要防止出现重复元素对应的情况
        s, t = t, s
        hashTable = {} # 声明字典
            
        for i in range(len(s)):
            if s[i] not in hashTable:
                hashTable[s[i]] = t[i]
            if hashTable[s[i]] != t[i]:
                return False
            
        return True