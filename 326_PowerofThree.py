#neems code
#time is O(log to the base 3 n) cuz the loop is dividing by 3, if it was dividing by 3 it would be to the base 2
#space is O(1)
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<1):
            return False
        while n%3==0:
            n=n/3
        return n==1
    
#best code
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3**19% n== 0

#time and space is O(1)
#This is an optimized mathematical solution that avoids loops or recursion.
# It’s valid because 3¹⁹ is the maximum power of 3 within 32-bit integer limits.

        