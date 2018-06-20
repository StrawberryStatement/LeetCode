# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:20:59 2018

766. Toeplitz Matrix

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512

两对角不用处理
@author: trick150
"""
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row=len(matrix)
        col=len(matrix[0])
        for i in range(row-1):
            for j in range(col-1):
                if a[i][j]!=a[i+1][j+1]:
                    return False
        return True