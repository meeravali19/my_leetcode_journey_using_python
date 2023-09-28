class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                
                if i>0:
                    temp=nums[k]
                    nums[k]=nums[i]
                    nums[i]=temp
                    k+=1
                else:
                    k+=1
                    
        return nums



        
