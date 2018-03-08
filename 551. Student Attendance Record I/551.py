class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 计数
        absent = 0
        late = 0
        for c in s:
            if c == 'A':
                absent += 1
                late = 0
            elif c == 'L':
                late += 1
            else:
                late = 0
            
            if absent > 1 or late > 2:
                return False
            
        return True