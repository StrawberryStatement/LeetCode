# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 07:51:43 2018
617   参考
@author: trick150
"""
class Solution(object):  
    def mergeTrees(self, t1, t2):  
        if t1 and t2:  
            root = TreeNode(t1.val + t2.val)  
            root.left = self.mergeTrees(t1.left, t2.left)  
            root.right = self.mergeTrees(t1.right, t2.right)  
            return root  
        else:  
            return t1 or t2 