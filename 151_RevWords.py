class Solution(object):
    def reverseWords(self, s):
        s = s.strip()
        words = s.split()
        words.reverse()
        return " ".join(words)
#both are O(n)
# smaller code with same complexity
    class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])