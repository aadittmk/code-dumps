def namelist(names):
    '''
    https://www.codewars.com/kata/53368a47e38700bd8300030d
    namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
    # returns 'Bart, Lisa & Maggie'
    namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
    # returns 'Bart & Lisa'
    namelist([ {'name': 'Bart'} ])
    # returns 'Bart'
    namelist([])
    # returns ''
    '''
    if len(names) > 2:
        ret_str = ""
        for i in range(len(names)-2):
            for k, v in names[i].items():
                ret_str += v +", "
        names = names[-2:]
        for i in range(len(names)):
            for k, v in names[i].items():
                ret_str += v + " & "
        return ret_str[:-3]
    elif len(names) == 2:
        ret_str = ""
        for i in range(len(names)):
            for k, v in names[i].items():
                ret_str += v
            ret_str += " & "
        return ret_str[:-3]
    elif len(names) == 1:
        for k, v in names[0].items():
            return v   
    else:
        return ''
