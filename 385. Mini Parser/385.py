# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        # one line 
        # return eval(s)
        if s[0] != '[':
            return NestedInteger(int(s))
        
        
        l = 0 # l point to the start of a number substring
                  # r point to the end+1 of a number substring
        # initial a stack
        stack = []
        # initial current element
        curr = None
        # When meeting a '[', we start recording current element. 
        # When meeting a ']', finish recording
        for r in range(len(s)):
            if s[r] == '[':  # append
                if curr:
                    stack.append(curr)
                curr = NestedInteger()
                l = r + 1
            elif s[r] == ',':
                if s[r-1] != ']':
                    curr.add(NestedInteger(int(s[l:r])))
                l = r + 1
            elif s[r] == ']': # pop
                if s[l:r]:
                    curr.add(NestedInteger(int(s[l:r])))
                if stack:
                    pop = stack.pop()
                    pop.add(curr)
                    curr = pop
                l = r + 1
                
        return curr
                
            

        