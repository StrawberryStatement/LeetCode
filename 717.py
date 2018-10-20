# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 21:24:46 2018
717. 1-bit and 2-bit Characters
@author: Trick150
"""

class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        one=0
        for i in range(len(bits)-2,-1,-1):
            if bits[i]==1:
                one+=1
            else:
                break
        if one%2==0:
            return True
        return False
        
        