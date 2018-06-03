# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 22:18:37 2018
832_resolve2
@author: trick150
"""

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A)==0:
            return A
        res=[]
        for row in A:
            res.append([])
            for col in row[::-1]:
                res[-1].append(1-col)
        print(res)
        return res        
        
A=[[1,1,0],[1,0,1],[0,0,0]]
a=Solution()
a.flipAndInvertImage(A)