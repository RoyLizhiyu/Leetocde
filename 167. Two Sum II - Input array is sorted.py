class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ptr1 = 0
        ptr2 = len(numbers) - 1
        
        while (numbers[ptr1] + numbers[ptr2]) != target:
            val = numbers[ptr1] + numbers[ptr2]
            if val > target:
                ptr2 -= 1
            
            elif val < target:
                ptr1 += 1
        return [ptr1+1, ptr2+1]
        
