def sum_dig_pow(a, b):
    '''
    https://www.codewars.com/kata/5626b561280a42ecc50000d1
    '''
    fin_list = []
    for iterator in range(a, b+1):
        res = [int(x) for x in str(iterator)]
        power = 0
        for _ in range(len(res)):
            power += 1
            res[_] = res[_] ** power
        if sum(res) == iterator:
            fin_list.append(iterator)
    return fin_list
