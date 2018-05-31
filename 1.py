# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:17:54 2018

@author: trick150
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        L=[]
        for i in nums:
            L.append(nums.index(i))
            other_num=target-i
            for j in nums[nums.index(i)+1:]:
                if(other_num==j):
                    L.append(nums[nums.index(i)+1:].index(j)+nums.index(i)+1)
                    print(L)
                    return(L)                
            L=[]
                    
       
nums = [3, 3]
target = 6           
a=Solution()
a.twoSum(nums,target)