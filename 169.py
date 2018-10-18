# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:30:24 2018

169. Majority Element

@author: Trick150
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        for i in s:
            count=0
            for j in nums:
                if j==i:
                    count+=1
            if count>len(nums)/2:
                return i
        return 0
