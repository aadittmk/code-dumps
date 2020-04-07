def row_sum_odd_numbers(n):
    '''
    https://www.codewars.com/kata/55fd2d567d94ac3bc9000064
    '''
    t = 0
    for i in range(1, n + 1):
        t += i
    l = [i for i in range(t + t) if i % 2 != 0]
    return sum(l[-n:])
