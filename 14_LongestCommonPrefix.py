class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        if strs[0] == strs[-1]:
            return strs[0]
        leng=min(len(strs[0]),len(strs[-1]))
        pre=""
        k=0
        first=strs[0]
        last=strs[-1]
        while k<leng:
            if first[k]==last[k]:
                k=k+1
            else:
                break
        return first[:k]

#  Time Complexity: O(n*m*log n), to sort the array, where n is the number of strings and m is the length of longest string.
# Auxiliary Space: O(m) to store the strings first, last and result           

        