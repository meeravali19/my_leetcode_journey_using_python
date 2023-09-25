class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = collections.Counter(s)

        for i, c in enumerate(t):
            count[c] -= 1
            if count[c] == -1:
                return c 
        
