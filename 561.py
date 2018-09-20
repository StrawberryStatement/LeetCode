# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 23:05:04 2018
561
@author: trick150
"""
from functools import reduce
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        #sort 函数返回NoneType
        #sum  已经可以将list中元素全部相加
        return sum(nums[::2])
a=Solution()
print(a.arrayPairSum([1,4,3,2]))