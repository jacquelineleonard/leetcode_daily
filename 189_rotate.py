class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        nums.reverse()
        
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        
        # O(n), O(1)