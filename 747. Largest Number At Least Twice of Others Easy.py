class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        maxIndex = nums.index(m)
        for i in range(len(nums)):
            if nums[i] != m and m < 2 * nums[i]:
                return -1
        return maxIndex
