class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=[]
        a=[]
        for i in range(len(nums)):
            s.append(nums[i])
            a.append(nums[i])
        z=s+a
        return z
        
