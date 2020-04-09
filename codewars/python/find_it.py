from collections import Counter
def find_it(seq):
    '''
    https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
    '''
    for k, v in Counter(seq).items():
        if v % 2 != 0:
            return k
