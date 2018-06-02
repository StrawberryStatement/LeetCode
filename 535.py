# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 21:32:11 2018
535
@author: trick150
"""

class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        return str(longUrl).replace(".com","*")
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        print(str(shortUrl).replace("*",".com"))
        return str(shortUrl).replace("*",".com")

# Your Codec object will be instantiated and called as such:
url="https://leetcode.com/problems/design-tinyurl"
codec = Codec()
codec.decode(codec.encode(url))    