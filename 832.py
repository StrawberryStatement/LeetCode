# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 15:22:46 2018
832
@author: trick150
"""
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        #用下标做，感觉不够python...
        for i in range(len(A)):
            A[i]=A[i][::-1]        
        for j in range(len(A)):
            for k in range(len(A[j])):
                A[j][k]=1-A[j][k]
        print(A)
        return A
A=[[1,1,0],[1,0,1],[0,0,0]]
a=Solution()
a.flipAndInvertImage(A)