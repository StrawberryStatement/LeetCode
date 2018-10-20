# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 18:55:03 2018
217. Contains Duplicate
@author: Trick150
"""

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if len(nums)>len(set(nums)) else False 