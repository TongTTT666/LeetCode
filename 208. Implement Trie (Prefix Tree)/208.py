class TrieNode:   # 把节点类要构建好
    def __init__(self):
        self.isword = False   # 判断这个节点是否代表一个终止
        self.child = {}  # 用字典去写儿子节点，因为可能会有很多儿子节点


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 初始化就是创建根节点，初始化Trie(字典树)只有根节点
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        # 过一遍这个单词，如果对应的节点的子节点没有该字母，则添加
        # 先声明根节点
        node = self.root
        for c in word:
            if c not in node.child:   # {}是字典，c in 字典就是字典中是否有c这个key值
                node.child[c] = TrieNode() # 指向下一个节点
            node = node.child[c]  # 弄到下一个节点
        node.isword = True  # 最后一个节点要标记是单词，搜索的时候要用
            
            
            
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        # 就不断地找对应的子节点，然后看最后一个节点的isword是否为True
        node = self.root
        for c in word:
            if c not in node.child:
                return False
            node = node.child[c]
        return node.isword
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node.child:
                return False
            node = node.child[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)