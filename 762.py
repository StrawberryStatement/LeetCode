# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 17:12:14 2018

762. Prime Number of Set Bits in Binary Representation

@author: trick150
"""

class Solution:                
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        count=0
        l=[2,3,5,7,11,13,17,19]
        sumNums = (bin(n).count('1') for n in range(L, R+1))
        for i in sumNums:
            if i in l:
                count+=1
                #print(str(i)+"  "+bin(i)[2:]+"  "+str(count))
        return count
a=Solution()
b=a.countPrimeSetBits(268280,269083)
print(b)