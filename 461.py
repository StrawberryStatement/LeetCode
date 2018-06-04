# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 08:24:43 2018

461

@author: trick150
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a=len(bin(x))
        b=len(bin(y))
        diff_bit=a-b if a>b else b-a
        res=0
        #bin(x)eg:{3:0b11,4:0b100},you need to remove "0b"
        for i in zip(bin(x)[2:][::-1],bin(y)[2:][::-1]):
            if(i[0]!=i[1]):
                res+=1
        for i in bin(x)[2:2+diff_bit] if a>b else bin(y)[2:2+diff_bit]:
            #print(i)
            res+=int(i) 
        print(res)
        return res
a=Solution()
x=1
y=4
a.hammingDistance(x,y)
        