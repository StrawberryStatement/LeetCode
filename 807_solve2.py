# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 10:48:47 2018

@author: trick150
"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_max=[max(i) for i in grid]
        col_max=[max(i) for i in zip(*grid)]
        return (sum(min(row_max[i],col_max[j])-grid[i][j] for i in range(len(row_max)) for j in range(len(col_max)) 
                )
                )            
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
a=Solution()
a.maxIncreaseKeepingSkyline(grid)