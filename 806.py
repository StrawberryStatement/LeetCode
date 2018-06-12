# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 15:16:06 2018

@author: trick150
"""

'''
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"
输出: [2, 4]
解释: 
除去字母'a'所有的字符都是相同的单位10，并且字符串 "bbbcccdddaa" 将会覆盖 9 * 10 + 2 * 4 = 98 个单位.
最后一个字母 'a' 将会被写到第二行，因为第一行只剩下2个单位了。
所以，这个答案是2行，第二行有4个单位宽度。
'''
class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        res=[1,0]
        for i in S:
            next_startnum=widths[ord(i)-ord("a")]
            res[1]+=next_startnum
            if res[1]>100:
                res[1]=next_startnum
                res[0]+=1
        print(res)
        return res  
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
a=Solution()
a.numberOfLines(widths,S)      