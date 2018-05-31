# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:04:48 2018

@author: trick150
"""

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=0
        for i in tuple(J):
            for j in tuple(S):
                if i == j:
                    count+=1
        print(count)
        return count
J = "aA"
S = "aAAbbbb"

a=Solution()
a.numJewelsInStones(J,S)