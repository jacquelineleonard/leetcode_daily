#my code
#time is O(n)
#space is O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num1=list(set(nums))
        return (len(num1)!=len(nums))
    
