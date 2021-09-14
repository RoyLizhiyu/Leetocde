class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        result = []
        
        #height
        m = len(mat)
        #width
        n = len(mat[0])
        
        #calculate the total number of diagonals
        num_d = m + n - 1
        
        # iterate 
        for diagonal_head in range(num_d):
            current_diagonal = []
            x = 0
            y = 0
            
            # set the indices of the head
            # first half of the diagonals, head is always in the first row, so 
            # x is always 0, and the vertical coordinate always increment by 1 
            # each iteration. So y is the current round of loop index(diagnoal             # head)
            if diagonal_head < n:
                x= 0
                y = diagonal_head
                
            # second half of the diagonals 
            else:
                x = diagonal_head - n + 1
                y = n - 1
            
            while x < m and y > -1:
                current_diagonal.append(mat[x][y])
                x += 1
                y -= 1
            if diagonal_head % 2 == 0:
                result.extend(current_diagonal[::-1])
            else:
                result.extend(current_diagonal)
                
        return result
            
