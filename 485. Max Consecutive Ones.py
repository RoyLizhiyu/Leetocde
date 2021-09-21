class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ptr1 = 0
        ptr2 = 1
        if len(nums) == 1:
            if nums[0] == 0:
                return 0
            else:
                return 1
            
        result = 0
        
        while ptr1 < len(nums):
            
            if nums[ptr1] == 1:
                current = 1
                while ptr2 < len(nums) and nums[ptr2] != 0:
                    ptr2+=1
                    current += 1
                    
                result = max(result, current)
                
                if ptr2 == len(nums):
                    break
                ptr1 += 1
                
            elif nums[ptr1] == 0:
                ptr1 += 1
                ptr2 = ptr1+1
            
        return result
