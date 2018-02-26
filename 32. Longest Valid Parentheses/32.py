# 法1： 动态规划（更重要）

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        # 最长有效子字符串是连续的！！！
        # 方法1：动态规划
        # 定义动态规划变量dp
        # dp[i]含义：以s[i]为结尾的最长有效字符串长度
        dp = [0] * len(s)
        for i in range(1, len(s)):
            # 如果s[i]是左括号，则肯定不是结尾，所以dp[i]=0
            if s[i] == '(':
                dp[i] = 0
            else:
                # 如果s[i]是右括号，s[i-1]是左括号，则刚好配齐
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                else:
                    # 如果s[i-1]是右括号则需要找到前一个有效子字符串前面的
                    # 那个字符看其是否为左括号，根据不同情况再判断
                    # 必须保证大于0才可以
                    # 前面一个判断是必须的，否则python中s[-1]默认访问栈顶元素
                    if i-1-dp[i-1] >= 0 and s[i-1-dp[i-1]] == '(':
                        # 产生匹配，注意子句的连贯性
                        dp[i] = dp[i-1] + 2 + dp[i-1-dp[i-1]-1]
        return max(dp)
                    

# 法2：用一个栈来解决（更简单）

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        # 最长有效子字符串是连续的！！！
        # 方法2：用栈
        # 目的：找到不能被匹配的符号的index
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                # 如果s[i]是左括号，直接入栈等待匹配
                # 技巧！推下标！不是推字符！
                stack.append(i)
            else:
                # 如果是右括号，则访问栈顶元素
                # 如果栈顶元素是左括号，则出栈匹配
                # 如果栈顶元素不是左括号或者栈是空的，则把右括号入栈
                # 因为其根本无法匹配，也是一个待匹配元素
                # stack[-1]是栈顶元素
                # 习惯：出栈就要判断栈是否为空
                if stack:
                    if s[stack[-1]] == '(':
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
        
        print(stack)
        # 至此，stack中保存的就是那些最终都无法匹配的括号的对应下标
        # 最长连续子字符串的长度就是这些相邻下标差值最大的那个再减1
        # 技巧：错位相减！！！头尾补-1和len(s)，注意！这个地方stack中的数字类似于间断符！
        # 默认的无法匹配字符应该是头元素的前一个下标与尾元素的后一个下标（空字符），而不是头元素和尾元素的下标
        # 如果stack是空的，那么不存在不能匹配的元素，我们就直接返回原字符串长度
        if not stack:
            return len(s)
        
        
      
        return max(x-y-1 for x, y in zip(stack + [len(s)], [-1]+stack))
        
                        
                    
                    