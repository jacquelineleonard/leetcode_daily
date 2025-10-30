#neems code
#time and space is O(n)
#where n is no. of digits of x
#so best case would be single digit
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        return s==s[::-1]
        
#best soln - no converting to string but halfing the no. and then comparing
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10

#time is O(log₁₀(n))
#space is O(1)