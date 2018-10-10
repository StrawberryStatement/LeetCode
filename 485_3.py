# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:38:53 2018

485. Max Consecutive Ones

@author: Trick150

"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=0
        m=0
        for i in range(len(nums)):
            if nums[i]==1:
                n+=1
            else:
                m=max(m,n)
                n=0
        return max(m,n)