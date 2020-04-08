def expanded_form(num):
    '''
    https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python
    expanded_form(12) # Should return '10 + 2'
    expanded_form(42) # Should return '40 + 2'
    expanded_form(70304) # Should return '70000 + 300 + 4'
    '''
    temp = []
    num = str(num)
    for i in range(len(num)):
        temp.append(int(num[i]))
        
    temp = temp[::-1]
    cou = 10
    for i in range(1, len(temp)):
        temp[i] = temp[i] * cou
        cou *= 10
    temp = temp[::-1]
    
    num = ""
    for i in range(len(temp)):
        if temp[i] == 0:
            continue
        num += str(temp[i]) + " + "
    
    return num[:-3]
