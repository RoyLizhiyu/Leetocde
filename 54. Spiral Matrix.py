class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        up = 0
        left = 0
        right = len(matrix[0]) -1
        bot = len(matrix) - 1
        result = []

        while len(result) < len(matrix[0]) * len(matrix):
            # traverse from left to right, row fixed, column changing.
            for i in range(left, right+1):
                result.append(matrix[up][i])
            
            # traverse from top to down. row changing, column fixed.
            for i in range(up+1, bot+1):
                result.append(matrix[i][right])
                
            #traverse from right to left. Make sure we only traverse
            # the row we haven't been. That means we only go from right to left
            # when up and bot haven't become the same row.
        
            if up != bot:
                for i in range(right-1, left-1, -1):
                    result.append(matrix[bot][i])
            
            #travere from bot to up. Make sure we only traverse the column
            # we haven't been. That means we only go from bot to top when
            # left and right haven't become the same column.

            if left != right:
                for i in range(bot-1, up, -1):
                    result.append(matrix[i][left])
                    
            #update the pointers,, make sure they squeeze the rectangle
            up += 1
            left  += 1
            right -= 1
            bot -= 1
        return result
