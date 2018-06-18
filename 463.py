# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 17:22:48 2018

463. Island Perimeter

@author: trick150
"""
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        neb=[0,0,0,0]
        for i in grid:
            i.append(0)
            i.insert(0,0)
        grid.insert(0,[0]*(len(grid)+2))
        #len(grid)已经改变(+1)
        grid.append([0]*(len(grid)+1))  
        num=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                print(len(grid))
                if grid[i][j]==1:
                    if grid[i][j+1]==1:
                        num+=1
                    if grid[i][j-1]==1:
                        num+=1
                    if grid[i+1][j]==1:
                        num+=1
                    if grid[i-1][j]==1:
                        num+=1
                if num==1:
                    neb[0]+=1
                if num==2:
                    neb[1]+=1
                if num==3:
                    neb[2]+=1
                if num==4:
                    neb[3]+=1
                num=0
        return sum(sum(i) for i in grid)*4-neb[0]*1-neb[1]*2-neb[2]*3-neb[3]*4  
a=Solution()
b=a.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
) 
print(b)    