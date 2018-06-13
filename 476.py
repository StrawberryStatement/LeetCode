# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:34:56 2018
476
@author: trick150
"""
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        l=len(bin(num))-2 
        #base=2
        a=int("1"*l,2)
        return num^a
a=Solution()
print(a.findComplement(5))
