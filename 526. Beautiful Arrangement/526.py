# 法1： 超时
class Solution:
    
    def __init__(self):
        self.count = 0
        
    
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        # similar with N-queens
        # use recursive to obtain the final result
        # backtracking 
        used_number = [0] * N
        self.helper(used_number, 1, N)
        return self.count
        
            
    def helper(self, used_number, pos, N):
        '''
        used_number: record the number we have used
                    if uesd_number[i] = 1 that means number i+1 has been used
                    else means number i+1 has not been used yet
        pos: current position we are considering
        N: just the same as the argument N in countArrangement function
        '''

        if pos > N:
            self.count += 1
            return

        # we need to try every number between 1 and N
        for i in range(1, N+1):
            if used_number[i-1] == 0 and (i % pos == 0 or pos % i == 0):
                used_number[i-1] = 1
                self.helper(used_number, pos+1, N)
                # this number need to change
                used_number[i-1] = 0

        
# 法2：位置从后往前取推-》通过
class Solution:
    
    def __init__(self):
        self.count = 0
        
    
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        # similar with N-queens
        # use recursive to obtain the final result
        # backtracking 
        used_number = [0] * N
        self.helper(used_number, N, N)
        return self.count
        
            
    def helper(self, used_number, pos, N):
        '''
        used_number: record the number we have used
                    if uesd_number[i] = 1 that means number i+1 has been used
                    else means number i+1 has not been used yet
        pos: current position we are considering
        N: just the same as the argument N in countArrangement function
        '''

        if pos <= 0:
            self.count += 1
            return

        # we need to try every number between 1 and N
        for i in range(1, N+1):
            if used_number[i-1] == 0 and (i % pos == 0 or pos % i == 0):
                used_number[i-1] = 1
                self.helper(used_number, pos-1, N)
                # this number need to change
                used_number[i-1] = 0

        
        
        
        
        
        
        
        
      
        
        
        
        
        