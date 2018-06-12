# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 22:01:56 2018
811
@author: trick150
"""

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        word = []
        result = dict()
        output = []

        for temp in cpdomains:
            times = int(temp[:temp.index(' ')])
            url = temp[temp.index(' ')+1:]
            words = ''.join(url)                 # Convert to a string
            
            # From string to a list that contain every choice
            index_i = 0
            while index_i < len(words):
                word.append(words[index_i:])
                index_i = words.find('.',index_i,len(words)) + 1
                if index_i == 0:
                    break

            for temp1 in word:                   # add the result into the dict
                if temp1 in result:
                    result[temp1] += times
                else :
                    result[temp1] = times

            word.clear()
            times = 0
        
        for key,value in result.items():
            output.append(str(value) + ' ' + key)
        return output
l=["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
a=Solution()
print(a.subdomainVisits(l))
