# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 20:54:01 2018

896. Monotonic Array

@author: Trick150
"""

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        L=[]
        for i in range(len(A)-1):
            L.append(A[i+1]-A[i])
        print(sum(L))
        print(sum(map(abs,L)))
        if abs(sum(L)) != sum(map(abs,L)):
            return False
        else:
            return True
a=Solution()
b=[6,5,4,4]
print(a.isMonotonic(b))