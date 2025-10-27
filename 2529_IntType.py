# neems Code 
# time is O(n)
# space is O(1)
class Solution(object):
    def maximumCount1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        co=0
        c=0
        for x in nums:
            if x<0:
                c=c+1
            elif x>0:
                co=co+1
        
        return max(c,co)

#best code time O(logn) and space is O(1)
class Solution1(object):

    def lowerbound(self, nums, target): 
        left, right = -1, len(nums)

        while left + 1 < right: 
            mid = (left + right)//2
            if nums[mid] < target: 
                left = mid
            else: 
                right = mid 

        return right

    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sorted interger array
        start = self.lowerbound(nums, 0)
        end = self.lowerbound(nums, 1)

        return max(start, len(nums)-end)

    
        


        