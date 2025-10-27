class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        co=1
        arr=[]
        for i in sentences:
            words=i.split()
            co=len(words)
            arr.append(co)        

        max_val=max(arr)
        max_ind=arr.index(max_val)
        return arr[max_ind]
#neems code           
# Let L be the total number of words in all sentences combined.
# and n is the no. of sentences
# time : O(L + n)
# space :O(m+n)

#best code
class Solution1(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        b=[]
        for i in sentences:
            c=i.split(" ")
            b.append(len(c))
        return max(b)
