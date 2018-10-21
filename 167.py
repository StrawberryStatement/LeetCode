# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 13:53:45 2018
167. Two Sum II - Input array is sorted
@author: Trick150

Python双向指针的用法（拿下标当指针）
"""

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p0,p1=0,len(numbers)-1
        while True:
            value=numbers[p0]+numbers[p1]
            if value==target:
                return [p0+1,p1+1]
            elif value>target:
                p1-=1
            else:
                p0+=1
                

                    
numbers = [2,7,11,15]
target = 13
a=Solution()
print(a.twoSum(numbers,target))       