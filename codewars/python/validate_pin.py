def validate_pin(pin):
    '''
    https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
    '''
    if len(pin) != 4 and len(pin) != 6:
        return False
    else:
        if pin.isnumeric():
            return True
        else:
            return False
