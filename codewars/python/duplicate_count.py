from collections import Counter
def duplicate_count(text):
    '''
    https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
    "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
    "aA11" -> 2 # 'a' and '1'
    "abcde" -> 0 # no characters repeats more than once
    "aabbcde" -> 2 # 'a' and 'b'
    '''
    cou = 0
    for k, v in Counter(text.lower()).items():
        if v > 1:
            cou += 1
    return cou
