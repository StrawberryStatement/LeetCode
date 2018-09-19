# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 22:01:05 2018

136. Single Number  method 2
 
@author: trick150
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        temp=nums[0]
        count=0
        flag=0
        if len(num)==1:
            return num[0]
        else:
            for i in range(1,len(nums)):
                if temp==nums[i]:
                    #nums.remove(temp)
                    temp=nums[i]
                    flag=1
                else:
                    if flag==1:
                        flag=0
                        #nums.remove(temp)
                        temp=nums[i]
                        if i==len(nums)-1:
                            return temp
                    else:
                        return temp 
a=Solution()
b=a.singleNumber([4,3,4,1,2,1,2])   
print(b)     
                           
            
