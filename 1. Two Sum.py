class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        maps = {}
        for i in range(len(nums)):
            maps[nums[i]] = i
        for i in range (len(nums)):
            comp = target - nums[i] 
            if comp in maps and maps[comp] != i:
                return [maps[comp], i]
