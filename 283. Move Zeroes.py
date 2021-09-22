class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums) - j:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                j += 1
            else:
                i += 1
