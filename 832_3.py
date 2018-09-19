# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 17:01:35 2018

@author: Trick150

832. Flipping an Image
"""

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B=[i[::-1] for i in A]
        count=0
        C=[]
        D=[]
        for i in B: 
            for j in i:
                D.append(1-j)
            C.append(D)
            # list has no attr clear,do not lick c# or java
            D=[]
        return C