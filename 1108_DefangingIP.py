#neems code
#time and space is O(n)
#where n in length of string

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")

# A defanged IP address is a modified version of an IP address where the original dots (\(..\)) 
# are replaced with \(`[.]`\) to prevent it from being recognized as a clickable link or a functional address.
# This cybersecurity technique is used to safely share IP addresses in text form, such as in emails or online forums,
# so they don't trigger an automatic link and lead to accidental activation or malicious action. 