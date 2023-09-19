class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        y=len(set(nums))
        x=len(nums)
        if x != y:
            return True
        else:
            return False


        
