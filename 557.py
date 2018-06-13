# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 16:42:03 2018
557
@author: trick150
"""
class Solution():
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        for i in s.split(" "):
            l.append(i[::-1])
        print(l)
        s=" ".join(l)
        return s
a=Solution()
print(a.reverseWords("Let's take LeetCode contest"))