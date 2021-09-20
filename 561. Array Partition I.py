class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums.sort()
        l = 0
        r = 1
        while r < len(nums):
            val = min(nums[l], nums[r])
            result += val
            l += 2
            r += 2
        return result
