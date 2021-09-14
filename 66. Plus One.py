class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while i >= 0:
            # set all the nines to zero
            if digits[i] == 9:
                digits[i] = 0
                
            # meet no nine, increase it
            else:
                digits[i]+= 1
                return digits
            i -= 1
        # if the loop completes without returning anything, that means all the           digits are nines. In which case we append a [1] at the front.
        return [1]+ digits
