def alphabet_position(text):
    '''
    https://www.codewars.com/kata/546f922b54af40e1e90001da
    '''
    op = ""
    for i in text.lower():
        if ord(i) in range(97, 123):
            op += (str((ord(i) - 96)) + " ")

    return op[:-1]
