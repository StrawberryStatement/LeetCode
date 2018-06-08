# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 23:36:56 2018
728
@author: trick150
"""

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l=[]
        for i in range(left,right+1):
            flag=0
            for j in str(i):
                if int(j)==0 or i%int(j)!=0:
                    flag=1
            if flag==0:
                l.append(i)
        print(l)
        return l
a=Solution()
a.selfDividingNumbers(1,22)
            