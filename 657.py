# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 09:50:43 2018
657
@author: trick150
"""
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        a=[0,0]
        for i in moves:
            if i=="U":
                a[0]+=1
            if i=="D":
                a[0]-=1
            if i=="R":
                a[1]+=1
            if i=="L":
                a[1]-=1
        for i in a:
            if i!=0:
                print("false")
                return false
        print("true")
        return true
moves="LL"
a=Solution()    
a.judgeCircle(moves)