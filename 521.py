# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 19:20:41 2018
521. Longest Uncommon Subsequence I
is a interst question
Explaination：
If len(A)>len(B),longest substring is A,and no string in B contains A;
vice versa.If len(A)==len(B), if A!=B return len(A),else return -1 
@author: trick150
"""
class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return -1 if a==b else max(len(a),len(b))
