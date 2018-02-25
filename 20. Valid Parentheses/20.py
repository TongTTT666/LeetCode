class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 初始化一个栈，这题的符号满足栈的关系，也即
        # 后出现的左括号要与先出现的对应右括号匹配
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack:
                    tmp = stack.pop()
                    if c == ')': 
                        if tmp != '(':
                            return False

                    if c == ']':
                        if tmp != '[':
                            return False

                    if c == '}':
                        if tmp != '{':
                            return False
                else:
                    return False
            
        # 空的就说明所有的左括号找到了对应的右括号
        if not stack:
            return True
        else:
            return False
                    
                