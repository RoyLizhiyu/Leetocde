class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #merge nums1 + nums 2
        merge = []
        m = len(nums1)
        n = len(nums2)
        idx1 = 0
        idx2 = 0
        for i in range (m+n):
            if idx1 == m:
                merge.append(nums2[idx2])
                idx2 += 1
            elif idx2 == n:
                merge.append(nums1[idx1])
                idx1 += 1
            elif nums1[idx1] > nums2[idx2]:
                merge.append(nums2[idx2])
                idx2 += 1
                
            elif nums1[idx1] < nums2[idx2]:
                merge.append(nums1[idx1])
                idx1 += 1
            else:
                merge.append(nums1[idx1])
                idx1 += 1
                
        # find median
        
        if len(merge) % 2 == 0:
            m = len(merge) / 2
            val1 = float(merge[m])
            val2 = float(merge[m-1])
            result = float((val1 + val2) / 2)
            return result
        else:
            return merge[len(merge)/2]
