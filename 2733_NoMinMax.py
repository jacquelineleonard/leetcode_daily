#neems code
#time complexity is O(n+klogk)
#space is O(k)
class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num1=list(set(nums))
        num1.sort()
        x=len(num1)
        if x<=2:
            return -1
        else:
            return num1[1]
        
#best code
class Solution1(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_no, max_no = min(nums), max(nums)
        for num in nums:
            if num != min_no and num != max_no:
                return num
        return -1

#time is O(n)
#space is O(1)