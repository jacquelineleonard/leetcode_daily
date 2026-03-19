class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ind=-1
        i=0
        for x in nums:
            if x%10==i%10:
                ind=i
                break
            i=i+1
        return ind
# Mistake: stored/returned the value (x) instead of the index (i), and compared x % 10 with i directly;
# fix: return i and compare nums[i] % 10 == i % 10 since indices can exceed 9 but only their last digit matters.
#time is O(n) and space is O(1)