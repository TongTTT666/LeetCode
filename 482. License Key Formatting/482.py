# 法1： 太慢了
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # 先把该大写的都大写了，然后从后往前怼即可
        S = S.upper().replace('-', '')  # 用replace骚操作
        num = 0  # 统计当前一组的数字个数
        result = ""  # 结果字符串
        for i in range(len(S))[::-1]:
            if S[i] >= 'A' and S[i] <= 'Z' or S[i] >= '0' and S[i] <= '9':
                result = S[i] + result
                num += 1
                if num >= K:
                    num = 0
                    result = '-' + result
        if len(result) == 0:
            return ""
        if result[0] == '-':  # 有可能多加了一个，去掉即可
            return result[1:]
        return result


# 法2：用更快的办法，直接用余数确定第一组该有多少个
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # 先把该大写的都大写了，然后从后往前怼即可
        S = S.upper().replace('-', '')  # 用replace骚操作
        if len(S) == 0:
            return ""
        result = ""  # 结果字符串
        # 算一下还剩余了几个
        rem = len(S) % K
        result += S[:rem]
        num = 0 + rem  # 统计目前已经处理的字符
        while num < len(S):
            result += ('-' + S[num:num + K])
            num += K

        if result[0] == '-':
            return result[1:]
        return result