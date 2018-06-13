# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 22:16:34 2018
821 
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
                
                 
                
            
            
            
                
            
                     