class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        wordList = []
        
        ptr1 = 0
        while ptr1 < len(s):
            
            
            if s[ptr1] == ' ':
                ptr1 += 1
                continue
            
            else:
                ptr2 = ptr1
                while ptr2 < len(s) and s[ptr2] != ' ':
                    ptr2 += 1
                wordList.append(s[ptr1:ptr2])
                ptr1 = ptr2
                
        wordList.reverse()
        i = 0
        rev = ''
        while i < len(wordList):
            if i == 0:
                rev += wordList[i]
            else:
                rev += ' ' + wordList[i]
            i+= 1
        s = rev
        
        return s
                
