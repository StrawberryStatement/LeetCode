# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 09:33:50 2018

575. Distribute Candies

Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
The sister has three different kinds of candies. 

@author: trick150
"""
class Solution:
    def distributeCandies(candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        if len(set(candies))>=len(candies)/2:
            return len(candies)/2
        else:
            return len(set(candies))
