class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
           
        
#         if len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return 1
#         l = 1
#         r = 0
#         iList = []
#         while l < len(nums):
#             if nums[l] == nums[r]:
#                 if l == len(nums)-1:
#                     iList.append(nums[r])
                    
#             elif nums[l] != nums[r]:
#                 iList.append(nums[r])
#                 r = l
#                 if r == len(nums)-1:
#                     iList.append(nums[r])
#             l += 1
            
#         for i,k in enumerate(iList):
#             nums[i] = k
            
#         return len(iList)
            
            
