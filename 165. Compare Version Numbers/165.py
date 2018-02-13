class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        splitversion1 = version1.split('.')
        splitversion2 = version2.split('.')
        
        # 求一个最大长度，补齐即可
        max_length = max(len(splitversion1), len(splitversion2))
        
        
        
        # 分成点之前和点之后，但必须考虑长度，不够长度的补0
        if len(splitversion1) < max_length:
            while len(splitversion1) < max_length:
                splitversion1.append("0")
        else: 
            while len(splitversion2) < max_length:
                splitversion2.append("0")
        
        # 一层一层的比
        for i in range(max_length):  
            if int(splitversion1[i]) > int(splitversion2[i]):
                return 1
            elif int(splitversion1[i]) == int(splitversion2[i]):
                pass
            else:
                return -1
        
        return 0
            
        
        
        