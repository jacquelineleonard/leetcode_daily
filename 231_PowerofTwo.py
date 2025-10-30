#neems code
#time is O(log to the base 2 n), cuz divided by 2
#space is O(1)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        while(n%2==0):
            n=n/2
        return n==1
    
#best solution - asked for O(1) bitwise approach
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0
#interview points
#A power of 2 in binary has exactly one bit set (e.g., 1000 for 8).
#So, n & (n-1) clears that bit and becomes 0 only for powers of 2.