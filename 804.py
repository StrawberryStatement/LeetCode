# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 11:38:53 2018
804
@author: trick150
"""

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """       
        morse_code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha_list=list(map(chr,range(97,123)))
        morse_dict=dict(zip(alpha_list,morse_code))
        var=set()
        for i in words:
            str=""
            for j in i:
                str+=morse_dict[j]
            var.add(str)
        print(len(var))
        return len(var)
a=Solution()
words = ["gin", "zen", "gig", "msg"]
a.uniqueMorseRepresentations(words)               

