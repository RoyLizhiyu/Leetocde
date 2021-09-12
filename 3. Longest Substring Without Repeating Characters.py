class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        result = 0
        table = {}
        while right < len(s):
            
            #meet duplicate, retract left 
            if s[right] in table:
                del table[s[left]]
                left += 1
            
            #No duplicate, extend right
            else:
                table[s[right]] = 1
                result = max(result, right-left+1)
                right += 1
                
        
        return result
