# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 09:57:13 2018

412. Fizz Buzz

@author: trick150
"""

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                res.append("FizzBuzz")
            elif i%3==0:
                res.append("Fizz")
            elif i%5==0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
a=Solution()
b=a.fizzBuzz(15)
print(b)