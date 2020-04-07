from collections import Counter
class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter = 0
        for k, v in Counter(arr).items():
            if k+1 in Counter(arr).keys():
                if v == 1:               
                    counter += 1
                else:
                    counter += v
        return counter