class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ''
        while i >= 0 or j >= 0 or carry == 1:
            va1 = a[i] if i >= 0 else '0'
            va2 = b[j] if j >= 0 else '0'
            
            sum = int(va1) + int(va2) + carry
            if sum == 3:
                carry = 1
                result += '1'
            if sum == 2:
                carry = 1
                result += '0'
            if sum == 1:
                carry = 0
                result += '1'
            elif sum == 0:
                result += '0'
            
            i -= 1
            j -= 1
        result = result[::-1]
        return result
