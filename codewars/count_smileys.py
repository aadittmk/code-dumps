def count_smileys(arr):
    '''
    https://www.codewars.com/kata/583203e6eb35d7980400002a
    '''
    cou = 0
    for i in range(len(arr)):
        if (arr[i][0] == ":" or arr[i][0] == ";"):
            if len(arr[i]) == 3:
                if (arr[i][1] == "-" or arr[i][1] == "~") and (arr[i][-1:] == ")" or arr[i][-1:] == "D"):
                    cou += 1
            elif (arr[i][-1:] == ")" or arr[i][-1:] == "D"):
                cou += 1

    return cou
