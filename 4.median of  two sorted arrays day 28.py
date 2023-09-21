class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        s=[]
        s=nums1+nums2
        s1=sorted(s)
        c=len(s)
        
        if c%2==0:
             z=s1[(c//2)-1]+s1[(c//2)]
             v=float(z)/2
             return v
            
        else:
             print(s1)
             return s1[(c//2)]
