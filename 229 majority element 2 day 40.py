"""Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
"""
# program

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=[]
        k=[]
        for i in range(len(nums)):
            counter=0
            if nums[i] not in s:
                s.append(nums[i])
                for j in range(i,len(nums)):
                    if nums[i]==nums[j]:
                        counter+=1
                if counter>len(nums)/3:
                    k.append(nums[i])
        return k
