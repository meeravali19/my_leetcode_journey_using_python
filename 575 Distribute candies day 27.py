class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        x=len(candyType)
        y=x/2
        z=[]
        for i in range(x):
            if candyType[i] not in z and len(z)<y:
                z.append(candyType[i])
        return len(z)

        
