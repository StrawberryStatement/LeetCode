# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 21:24:46 2018
717. 1-bit and 2-bit Characters

思路：最后一个数一定是0；倒数第二个数开始，
如果倒数第二个数是0，那么return true ；
如果倒数第二个数是1：
向前找1，如果一共经过偶数个1后找到0，
那么最后一个0翻译成一位，其他11翻译成一个char；
如果经过奇数个1找到0，那么倒数两个数为10，
return false

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
        
        