class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            if nums[0] >= target:
                return 1
            else:
                return 0
        
        result = float('inf')
        
        left = 0
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            while sums >= target:
                result = min(result, i+1 - left)
                sums -= nums[left]
                left += 1
        if result == float('inf'):
            result = 0
        return result
