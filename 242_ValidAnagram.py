#neems code
#time is O(nlogn)
#space is O(n)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return(sorted(s)==sorted(t))
    

from collections import Counter

#best soln
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict

	 

	# Let n be the length of the longest word
	# Time complexity: O(n)
	# Space complexity: O(n)
#interview points
# Counter is a subclass of Python’s built-in dict from the collections module.
# It is used to count the frequency of each element in an iterable (like a string, list, or tuple).
# It returns a dictionary-like object where keys are elements and values are their counts.
	 