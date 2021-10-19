class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        result = []
        if numRows == 1:
            result.append([1])
            return result
        
        else:
            temp = self.generate(numRows-1)
            result.extend(temp)
            last_row = temp[-1]
            new = []
            i = 0
            j= 0
            
            while i <= len(last_row):
                if i == 0:
                    new.append(last_row[i])
                elif i == len(last_row):

                    new.append(last_row[-1])
                elif i > j:
                    new.append(last_row[i] + last_row[j])
                    j += 1
                
                
                i += 1
            result.append(new)
            return result
