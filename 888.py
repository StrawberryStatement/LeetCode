# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 17:03:05 2018
888. Fair Candy Swap
@author: Trick150

 We know the difference between two arrays.
 Lets call it diff.
 candy_alice is the candy alice gave to bob
 candy_bob is the candy bob gave to alice
 Alice's candy after exchange: sumA - candy_alice + candy_bob
 Bob's candy after exchange : sumB - candy_bob + candy_alice
 These two should equal after exchange:
 sumA - candy_alice + candy_bob = sumB - candy_bob + candy_alice
 use math we can get: sumA - sumB = 2*(candy_alice - candy_bob) = diff
 We can represent candy bob as: candy_alice - diff/2
 then, for each element in A, check if candy_alice - diff/2 is in B


"""

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        这个题要先把set(A)用变量表示出来
        直接放到循环里会报超时，不知道怎么回事
        """
        # calculate difference between A, B
        diff = sum(A) - sum(B)
        A = set(A)
        B = set(B)
        for item in A:
            item2 = item - diff/2
            if item2 in B:
                return [item,item2]
                    
                    