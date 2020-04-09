def DNA_strand(dna):
    '''
    https://www.codewars.com/kata/554e4a2f232cdd87d9000038
    '''
    compl_dna = ""
    dna_dict = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'}
    for i in dna:
        for k, v in dna_dict.items():
            if i == k:
                compl_dna += v

    return compl_dna
