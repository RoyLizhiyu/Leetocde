class Solution(object):

#         if len(needle) == 0:
#             return 0
#         if len(haystack) == 0:
#             return -1
#         for i,k in enumerate(haystack):
#             # if elements in haystack after i is not enough for                 # the needle.
#             if i + len(needle) > len(haystack):
#                 break
#             for j, h in enumerate(needle):
#                 if haystack[i+j] != needle[j]:
#                     break
                    
#                 if j == len(needle) -1:
#                     return i
#         return -1
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:             
            return -1
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i] != needle[0]:
                continue
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
