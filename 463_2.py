# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 19:01:29 2018

463_2 i don't know why this can work at leetcode

@author: trick150
"""

class Solution:
    
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int 
        """
        
        perimeter = 0
        arra = grid.copy()
        print(arra)
        arra.insert(0,[0]*(len(grid[0])+2))
        arra.append([0]*(len(grid[0])+2))
        print(arra)
        for i in range(1,len(arra)-1):
            arra[i].insert(0,0)
            arra[i].append(0)
        print(arra)
        
        for i in range(1,len(arra)-1):
            for j in range (1, len(arra[0])-1):
                if arra[i][j]==1:
                    if arra[i-1][j] ==0:
                        perimeter+=1
                    if arra[i][j-1] ==0:
                        perimeter+=1
                    if arra[i][j+1] ==0:
                        perimeter+=1
                    if arra[i+1][j] ==0:
                        perimeter+=1
        return perimeter  
a=Solution()
b=a.islandPerimeter([[1,0,0]]
) 
print(b)    