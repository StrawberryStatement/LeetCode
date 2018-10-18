# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:46:19 2018

122. Best Time to Buy and Sell Stock II

因为我们可以昨天买入，今日卖出，若明日价更高的话，还可以今日买入，明日再抛出
@author: Trick150
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                profit+=prices[i+1]-prices[i]
        return profit
