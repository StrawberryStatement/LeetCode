# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:28:04 2018
695. Max Area of Island
@author: Trick150
"""

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if i<=0 and i<m and j>=0 and j<n and grid[i][j]:
                grid[i][j]=0
                return 1+dfs(i-1,j)+dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1)
            return 0
        l=[dfs(i,j) for i in range(m) for j in range(n)]
        return max(l)

a=Solution()
l=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(a.maxAreaOfIsland(l))