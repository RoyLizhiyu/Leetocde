class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) -1
        
        while i < j:
            last = s[j]
            first = s[i]
            s[i] = last
            s[j] = first
            i += 1
            j -= 1
 
