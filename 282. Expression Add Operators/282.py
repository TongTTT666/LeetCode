class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        # decide the start number in num
        for i in range(1, len(num)+1):
            # giving initial argument 
            # 0XXXX... can not be a number, we should avoid this situation
            if i == 1 or (i > 1 and num[0] != '0'): 
                self.DFS(num[i:], num[:i], int(num[:i]), int(num[:i]), res, target)
        return res
        
        
        
    def DFS(self, re_num, op_str, cur_val, last_num, res, target):
        # re_num: the remaining numbers
        # op_str: the string of operation like "3+2*5"
        # cur_val: current value after calculate
        # last_num: record the last number with its sign using in multiplication
        # res: the result of this problem
        # target: target value
        
        # If all these number have been searched, decide whether satisfy the requirment of this problem
        if not re_num:
            if cur_val == target:
                res.append(op_str)
            # bottom situation
            return
        # There are three ways to search, that is '+', '-' and '*'
        for i in range(1, len(re_num)+1):
            # cur_num: current number (e.g. 10 in "105" or "1" in 105)
            cur_num = re_num[:i]
            # 0XXXX... can not be a number, we should avoid this situation
            if i == 1 or (i > 1 and re_num[0] != '0'): 
                # '+'
                self.DFS(re_num[i:], op_str + "+" + cur_num, cur_val+int(cur_num), int(cur_num), res, target)
                # '-'
                self.DFS(re_num[i:], op_str + "-" + cur_num, cur_val-int(cur_num), -int(cur_num), res, target)
                # '*'
                self.DFS(re_num[i:], op_str + "*" + cur_num, cur_val-last_num+last_num*int(cur_num), int(cur_num)*last_num, res, target)
            
            
            
            
            
            
            