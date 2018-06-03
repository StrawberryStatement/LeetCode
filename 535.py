# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 21:32:11 2018
535
@author: trick150
"""

class Codec:

    def __init__(self):
        self.urls=[]
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.urls.append(longUrl)
        return 'http://tinyurl.com/'+str(len(self.urls)-1)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.urls[int(shortUrl.split("/")[-1])]

# Your Codec object will be instantiated and called as such:
url="https://leetcode.com/problems/design-tinyurl"
codec = Codec()
codec.decode(codec.encode(url))    