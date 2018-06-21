# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 17:16:49 2018

136. Single Number 去重，超时 

@author: trick150
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        num_set=[i for i in set(nums)]
        for i in num_set:
            if i in nums:
                nums.remove(i)
        for i in num_set:
            if i not in nums:
                return i
a=Solution()
b=a.singleNumber([4,1,2,1,2])   
print(b)     
        
        