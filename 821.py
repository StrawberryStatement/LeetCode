# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 22:16:34 2018
821 
1.一次遍历，用一个与S等长数组保存好所有C字符所在的位置，数组对应位 置0，其余置一个大数（255）
2.比较位置差值，等长数组对应值置最小的abs值。
@author: trick150
"""

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        l=[]
        c_loc=[]
        for i in range(len(S)):
            if S[i]==C:
                c_loc.append(i)
                l.append(0)
            else:
                l.append(255)
        for i in c_loc:
             for j in range(len(l)):
                 if abs(i-j)<l[j]:
                     l[j]=abs(i-j)
        return l
s="loveleetcode"
c="e"
a=Solution()
print(a.shortestToChar(s,c))
                
                 
                
            
            
            
                
            
                     