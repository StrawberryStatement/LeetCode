# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:32:11 2018

485. Max Consecutive Ones

@author: Trick150
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(max(''.join([str(x) for x in nums]).split('0')))