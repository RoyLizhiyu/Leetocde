class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        total_sum = sum(nums)
        for i, val in enumerate(nums):
            right = total_sum - val - left
            if left == right:
                return i
            else:
                left += val
        return -1
