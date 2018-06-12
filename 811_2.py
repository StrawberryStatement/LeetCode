# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 21:47:18 2018
811_2
@author: trick150
"""


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        words=[]
        res_dic={}
        res=[]
        for item in cpdomains:
            start_num=0
            num=int(item.split(" ")[0])
            dom=item.split(" ")[1]
            while start_num<len(dom):
                words.append(dom[start_num:])
                start_num=dom.find(".",start_num)+1
                #找不到返回-1
                if start_num==0:
                    break
            for word in words:
                if word in res_dic:
                    res_dic[word]+=num    
                else:
                    res_dic[word]=num
            words.clear()
        for k,v in res_dic.items():
            res.append(str(v)+" "+ k)
        return res

l=["9001 discuss.leetcode.com"]
a=Solution()
print(a.subdomainVisits(l))
