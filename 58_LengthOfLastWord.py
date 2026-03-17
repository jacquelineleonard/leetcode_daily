class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=len(s)-1
        length=0

        while s[i]==" ":
            i=i-1
        while i>=0 and s[i]!=" ":
            length=length+1
            i=i-1
        return length
#time is O(n)
#space is O(1)