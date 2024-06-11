
def conv_int(num):
    return int(num)
def conv_abs(num):
    return abs(num)
def conv_float(num):
    return float(num)

types = {'Z': (conv_int,), 'N': (conv_int, conv_abs), 'Q': (conv_float,)}

def type_cast(data, datatype):
    for i in types[datatype]:
        data = i(data)
    return data