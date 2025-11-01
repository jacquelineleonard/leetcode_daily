#neems code
#time n space is O(1)
class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        #41+1=b
        #41+7=b
        return (ord(coordinates[0]) - ord('a') + int(coordinates[1])) % 2 == 0

# ord() in Python returns the Unicode code point (integer value) of a given character.
