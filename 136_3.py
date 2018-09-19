# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 23:40:03 2018

136. Single Number  3
every element appears twice except for one
attention

@author: trick150
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c=Counter(nums)
        for i in nums:
            if c[i]!=2:
                return i
a=Solution()
b=a.singleNumber([4,3,4,1,2,1,2])   
print(b)   