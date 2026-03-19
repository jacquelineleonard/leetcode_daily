class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fre={}
        nums.sort()
        i=0
        for num in nums:
            if num in fre:
                fre[num]+=1
            else:
                fre[num]=1
        return max(fre,key=fre.get)
# Time Complexity: O(n)
# Space Complexity: O(n)

#best code - boyer moore voting
class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
#spac is O(1) time is same
