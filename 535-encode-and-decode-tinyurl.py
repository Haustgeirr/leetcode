class Codec:
    encodedUrls = []
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.encodedUrls.append(longUrl)
        index = len(self.encodedUrls) - 1
        return "http://tinyurl.com/" + str(index)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        splitUrl = shortUrl.split("/")
        return self.encodedUrls[int(splitUrl[-1])]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

longUrl = "https://leetcode.com/problems/design-tinyurl"

codec = Codec()
encoded = codec.encode(longUrl)
print(encoded)

decoded = codec.decode(encoded)
print(decoded)