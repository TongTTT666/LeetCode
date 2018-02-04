class Solution:
    def findTheDifference(self, s, t):
        c = 'a'
        while c <= 'z' and c >= 'a':
            if s.count(c) != t.count(c):
                return c
            c = chr(ord(c) + 1)