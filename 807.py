# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 15:56:21 2018

@author: trick150
"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        tans_grid=list(list(zip(*grid))[i] for i in range(len(grid)))
        row_max=[max(i) for i in grid]
        col_max=[max(i) for i in tans_grid]
        L_max=[]
        for i in row_max:
            L_temp=[]
            for j in col_max:
                L_temp.append(min(i,j))
            L_max.append(L_temp)
        print(L_max)
        a=sum(sum(L_max[i]) for i in range(len(L_max)))
        b=sum(sum(grid[i]) for i in range(len(grid)))
        print(a-b)
        return a-b
            
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
a=Solution()
a.maxIncreaseKeepingSkyline(grid)
        
        