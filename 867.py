# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:20:09 2018

@author: Trick150

867. Transpose Matrix
"""
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        l=[]
        k=[]
        for i in range(len(A[0])):
            for j in range(len(A)):
                k.append(A[j][i])
            l.append(k)
            k=[]
        return l
a=Solution()
l=[[1,2,3],[4,5,6],[7,8,9]]
print(a.transpose(l))