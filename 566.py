# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:39:11 2018

566. Reshape the Matrix

@author: trick150
"""

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        res=[]
        onedim_list=[i for item in nums for i in item]
        if len(nums)*len(nums[0])==r*c:
            for i in range(r):
                l=[]
                for j in range(c):
                    l.append(onedim_list[i*c+j])
                res.append(l)                    
            return res
        else:
            return nums
nums = [[1,2],[3,4]]
a=Solution()
b=a.matrixReshape(nums,2,4)
print(b)