# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 17:42:18 2018

500
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
500
@author: trick150
"""

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        l=['qwertyuiop','asdfghjkl','zxcvbnm']
        #l='asdfghjkl'
        for i in words: 
            for k in l:
                for j in i.lower():                
                    in_arow=0
                    if j not in k:
                        in_arow=1
                        break
                if in_arow==0:
                    res.append(i)
        return res
a=Solution()
print(a.findWords(["Hello", "Alaska", "Dad", "Peace"]))                
                
                