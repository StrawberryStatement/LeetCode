# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 15:58:45 2018

@author: Trick150

905. Sort Array By Parity
"""
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        start,end=0,len(A)-1
        while start<end:
            # swap odd and even num
            if A[start]%2==1 and A[end]%2==0:
                A[start],A[end]=A[end],A[start]
            #need not to handle
            elif A[start]%2==0:
                start+=1
            elif A[end]%2==1:
                end-=1
            else:
                start+=1
                end-=1
        return A
a=Solution()
b=[3,1,2,4]
print(a.sortArrayByParity(b))

