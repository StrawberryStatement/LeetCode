# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:16:36 2018

283. Move Zeroes

@author: Trick150
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num=0
        for i in range(len(nums)):
            if nums[i]!=0:
                buffer=nums[i]
                nums[i]=0
                nums[num]=buffer
                num+=1
        print(nums)
a=Solution()
l=[0,1,0,12,3]
l1=[0,0,1]
a.moveZeroes(l)