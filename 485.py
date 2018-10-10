# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:27:19 2018

485. Max Consecutive Ones

@author: Trick150
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        l=[]
        if sum(nums)==0:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i]==1:
                    count+=1
                    l.append(count)
                else:
                    count=0
        return max(l) if len(nums)>1 else 1
a=Solution()
b=[0,1]
print(a.findMaxConsecutiveOnes(b))