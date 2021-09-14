class Solution:
    def longestPalindrome(self, s):
        if len(s) < 1:
            return s

        def isPalindrome(left, right):
            return s[left:right] == s[left:right][::-1]

        left, right = 0, 1
        for index in range(1, len(s)):
            if index - right > 0 and isPalindrome(index - right - 1, index + 1):
                left, right = index - right - 1, right + 2
            if index - right >= 0 and isPalindrome(index - right, index + 1):
                left, right = index - right, right + 1
        return s[left: left + right]
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         #generate 2-d boolean array 
#         dp = [[False for j in range(len(s))] for i in range(len(s))]
        
#         result = '' 
#         # i = start point
#         i = len(s) - 1

        
#         while i >= 0:
#             # j = end point
#             j = i
#             while j < len(s):
                
#                 # S[i] equals S[j]
#                 #is_same = s[i] == s[j]
                
#                 # the current sub string from i to j is has at most 3                           characeters
#                 within_three = j - i < 3
#                 dp[i][j] = s[i] != s[j] and (within_three or dp[i+1][j-1])
                
#                 if dp[i][j] and (result is '' or j - i + 1 > len(result)):
#                     result = s[i:j+1]
#                 j+= 1
#             i-= 1
#         return result
