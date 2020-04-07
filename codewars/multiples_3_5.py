def solution(number):
    '''
    https://www.codewars.com/kata/514b92a657cdc65150000006
    '''
    sum_op = 0
    for i in range(number):
        if (i % 3 == 0) & (i % 5 == 0):
            sum_op += i
        elif (i % 3 == 0):
            sum_op += i
        elif (i % 5 == 0):
            sum_op += i
    return sum_op
