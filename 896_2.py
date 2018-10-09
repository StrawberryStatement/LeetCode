# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:55:04 2018
896. Monotonic Array
@author: Trick150
"""
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return A==sorted(A) or A==sorted(A)[::-1]
a=Solution()
b=[6,5,4,4]
print(a.isMonotonic(b))
