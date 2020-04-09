def sort_array(source_array):
    '''
    https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
    '''
    odd_list = []
    cou = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            odd_list.append(source_array[i])
            source_array[i] = "temp"
    odd_list.sort()
    for i in range(len(source_array)):        
        if source_array[i] == "temp":
            source_array[i] = odd_list[cou]
            cou += 1
    return source_array
