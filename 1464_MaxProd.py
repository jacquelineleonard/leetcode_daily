# neems Code 
# time is O(nlogn)
# space is O(1)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        x=len(nums)
        return ((nums[0]-1)*(nums[1]-1))

# best version
# time is O(n)
# space is O(1)
class Solution1(object):
    def maxProduct(self, nums):
        max1 = max2 = float('-inf')
        for n in nums:
            if n > max1:
                max2 = max1
                max1 = n
            elif n > max2:
                max2 = n
        return (max1 - 1) * (max2 - 1)

