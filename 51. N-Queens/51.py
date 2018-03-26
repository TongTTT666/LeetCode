class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # Every row or column must put only one queen
        # Thus, we only need to record the queen's position in every row or column
        
        # use DFS, search every points in the grid and find the valid points and recursive 
        # put one queen in one row
        '''
        There are three invalid situations: 
        If we put one queen in (x, y)
        1. any position (p, q) satisfied with p+q == x+y
        2. any position (p, q) satisfied with p-q == x-y
        3. any position (p, q) satisfied with x == p or y == q
        Since we only record the queen's position in every row(column) not the
        complete coordinate (x, y), the 3rd situation can be simplified to y == q(x == p)
        '''
        
        def DFS(queens, xSuby, xAddy):
            '''
            queens: the column number of queens in every row
            xsuby: save the invalid position satisfied with p-q == x-y
            xAddy: save the invalid position satisfied with p+q == x+y
            '''
            # determine which row is our current goal
            row = len(queens)
            # have finished the search process
            if row >= n:
                result.append(queens)
                return
                
            for col in range(n):
                # determine whether (row, col) is a valid position
                # if (row, col) is valid, continue searching, otherwise stop searching
                if col not in queens and row+col not in xAddy and row-col not in xSuby:
                    DFS(queens+[col], xSuby+[row-col], xAddy+[row+col])
            
        result = []
        DFS([],[],[])
        
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in one_solution] for one_solution in result]
                    
        
        