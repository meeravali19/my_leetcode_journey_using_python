class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def Sum(n):
            summ = 0
            while n:
                summ += pow(n % 10, 2)
                n //= 10
            return summ

        slow = Sum(n)
        fast = Sum(Sum(n))

        while slow != fast:
            slow = Sum(slow)
            fast = Sum(Sum(fast))

        return slow == 1
