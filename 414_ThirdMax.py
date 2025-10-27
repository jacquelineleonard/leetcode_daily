
#neems code

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #using set will remove the duplicates without retaining the order
        num1=list(set(nums))
        num1.sort(reverse=True)
        x=len(num1)
        if x<3:
            max_val=max(num1)
            return num1[num1.index(max_val)]
        else:
            return num1[2]
        
#to convert to set is O(n)
#then in set say k unique elements =O(k)
#total currently is O(n+k)
#sorting k elements is O(klogk)
#best case would be x<3 - O(n+klogk)
#worst case - O(n+klogk+k)
#since k<=n
#time complexity = O(nlogn)

#space complexity = O(k)=O(n)

#best code
#time - O(n)
#space - O(1)
class Solution1(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = float('-inf')
        
        for n in nums:
            if n == first or n == second or n == third:
                continue
            if n > first:
                third = second
                second = first
                first = n
            elif n > second:
                third = second
                second = n
            elif n > third:
                third = n
                
        return third if third != float('-inf') else first
