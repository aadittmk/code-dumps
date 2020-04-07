class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == (1 or 7):
            return True    
        a, b = n, n    
        while a > 9:
            a = 0
            while b > 0:
                c = 0
                c = b % 10
                a += c ** 2
                b /= 10
            if a == 1:
                return True
            b = a
        if a == 7:
            return True
        return False
