# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 11:25:43 2018

@author: Trick150

905. Sort Array By Parity
"""

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        
        sorted:built-in function :
        sorted(iterable, /, *, key=None, reverse=False)
        Return a new list  in ascending order.
        """

        print(sorted(A,key=lambda x:x%2==1,reverse=True))
        return sorted(A,key=lambda x:x%2)
a=Solution()
b=[3,1,2,4]
a.sortArrayByParity(b)