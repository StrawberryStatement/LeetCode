# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:22:37 2018

496. Next Greater Element I

@author: trick150
"""

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in nums1:
            flag=0
            for j in nums2[nums2.index(i):]:
                if j>i:
                    flag=1
                    res.append(j)
                    break
                #break
            if flag==0:
                res.append(-1)
        return res
a=Solution()
b=a.nextGreaterElement([4,1,2],[1,3,4,2])
print(b)            