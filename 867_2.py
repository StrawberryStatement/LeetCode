# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 16:33:47 2018

@author: Trick150

867. Transpose Matrix
"""
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        #*用法：把iter中所有参数当做位置参数依次传入，这个有点忘了
        return list(zip(*A))
a=Solution()
l=[[1,2,3],[4,5,6],[7,8,9]]
print(a.transpose(l))