import numpy as np

def xor(a, b):
    return [i ^ j for i, j in zip(a, b)]

def encode(data_input , key):
    data = data_input[:]
    temp = data + [0, 0, 0]

    if data[0] == 1:
        m = [1]
        temp = xor(temp, key)
    else:
        m = [0]
        temp = xor(temp, [0, 0, 0, 0])

    for _ in range(3):
        temp = temp[1:] + [0]
        if temp[0] == 1:
            m.append(1)
            temp = xor(temp, key)
        else:
            m.append(0)
            temp = xor(temp, [0, 0, 0, 0])

    print("Remainder: ", temp)
    data_crc = data + temp[1:]
    print("encoded Data with CRC: ", data_crc)
    return data_crc

def decode(data_input , key):
    data = data_input[:]
    temp = data

    if data[0] == 1:
        m = [1]
        temp = xor(temp, key)
    else:
        m = [0]
        temp = xor(temp, [0, 0, 0, 0])

    for _ in range(3):
        temp = temp[1:] + [0]
        if temp[0] == 1:
            m.append(1)
            temp = xor(temp, key)
        else:
            m.append(0)
            temp = xor(temp, [0, 0, 0, 0])

    print("Remainder: ", temp)
    return temp[1:]

data_input = [int(x) for x in input("Enter data bits separated by space: ").split()]
key = [int(x) for x in input("Enter the key separated by space: ").split()]
encode(data_input,key)

encode_data_input = [int(x) for x in input("Enter encoded data bits separated by space: ").split()]
if decode(encode_data_input,key) == [0,0,0]:
    print("no error")
else:
    print("error")