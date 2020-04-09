def unique_in_order(iterable):
    '''
    https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
    unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
    unique_in_order([1,2,2,3,3])       == [1,2,3]
    '''
    temp = []
    fin = []
    if type(iterable) == str:
        for iters in iterable:
            temp.append(iters)        
    else:
        temp = iterable
    
    for i in range(len(temp)):
        try:
            if temp[i] != temp[i+1]:
                fin.append(temp[i])
        except:
            fin.append(temp[i])
                
    return fin
