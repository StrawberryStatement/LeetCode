# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 10:29:13 2018

682. Baseball Game

Input: ["5","2","C","D","+"]
Output: 30

@author: trick150
"""
class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res=[]
        points=[]
        for i in ops:
            #isdigit()不支持负数判断，要自行定义
            if i.lstrip('-').isdigit():
                points.append(int(i))
                res.append(sum(points))
            if i=='C':
                points.remove(points[-1])
                res.remove(res[-1])
            if i=='D':
                points.append(2*points[-1])
                res.append(sum(points))
            if i=="+":
                points.append(points[-1]+points[-2])
                res.append(sum(points))
            print(res[-1])
        return res[-1]
a=Solution()
b=a.calPoints(["5","-2","4","C","D","9","+","+"])
print(b)
                
