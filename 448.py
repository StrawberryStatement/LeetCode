# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:00:03 2018

448. Find All Numbers Disappeared in an Array

do it without extra space and in O(n) runtime

@author: Trick150
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l={i+1 for i in range(len(nums))}
        for i in nums:
            if i in l:
                l.remove(i) 
        return list(l)
a=Solution()
l=[4,3,2,7,8,2,3,1]
print(a.findDisappearedNumbers(l))       