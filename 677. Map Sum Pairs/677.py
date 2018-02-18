class TrieNode:
    def __init__(self):
        self.isword = False
        self.val = 0
        self.child = {}


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.keys = {} # 记录已经出现过的单词和其对应的值
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        # 要克服覆盖情况，要记录已出现的单词和其对应的值
        if key in self.keys:
            temp = self.keys[key]
        else:
            temp = 0
        # 记录
        self.keys[key] = val
        
        # 实际的更改值是减去原有值加上新值，这是一个覆盖过程
        dif = val - temp
        
        
        node = self.root
        node.val += dif
        for c in key:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c] 
            node.val += dif
        node.isword = True
        

        
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        _sum = 0
        for c in prefix:
            if c not in node.child:
                return 0
            node = node.child[c]
        return node.val
            
        
        
# 用trie字典树结构

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)