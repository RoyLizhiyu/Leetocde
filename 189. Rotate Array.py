class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        table1= {}
        
        for key, val in enumerate(nums):
            table1[key] = val
        
        table2 = table1.copy()
        for key in table1:
            new_position = (key+k)%len(nums)
            table2[new_position] = table1[key]
        
        i = 0
        while i < len(nums):
            nums[i] = table2[i]
            i += 1
            
