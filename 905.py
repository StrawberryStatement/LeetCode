# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:54:32 2018

@author: Trick150

905. Sort Array By Parity
"""

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B=[]
        for i in range(len(A)):
            if A[i]%2==0:
                B.append(A[i])
                A[i]=0
        for i in A:
            if i !=0:
                B.append(i)
        print(B)
        return B
a=Solution()
b=[3,1,2,4]
a.sortArrayByParity(b)