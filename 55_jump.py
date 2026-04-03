class Solution(object):
    def canJump(self, nums):
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            if i + nums[i] > maxReach:
                maxReach = i + nums[i]
        return True