def move_zeros(array):
    '''
    https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
    move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
    '''
    res = list(filter(lambda a: a != 0 or type(a) == bool, array))
    for i in range(len(array)-len(res)):
        res.append(0)
    return res
