class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        head = strs[0]
        i = 1
        while i < len(strs):
            while strs[i].find(head) != 0:
                head = head[:-1]
                if head == '':
                    return ""
            i += 1
        return head
