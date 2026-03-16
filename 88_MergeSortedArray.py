class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        f = nums1[:m]
        f.extend(nums2)
        f.sort()

        for i in range(len(f)):
            nums1[i] = f[i]


# Time Complexity: O((m + n) log(m + n))
# Space Complexity: O(m + n)

# best code
class Solution(object):
    def merge(self, nums1, m, nums2, n):

        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

# Time: O(m + n)

# Space: O(1)        