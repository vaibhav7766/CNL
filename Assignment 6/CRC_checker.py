def xor(a, b):
    return [i ^ j for i, j in zip(a, b)]


def encode(data_input, key):
    data = data_input[:]
    temp = data + [0] * (len(key) - 1)
    for i in range(len(data)):
        if temp[i] == 1:
            temp[i : i + len(key)] = xor(temp[i : i + len(key)], key)

    remainder = temp[len(data) :]
    print("Remainder: ", remainder)
    data_crc = data + remainder
    print("Encoded Data with CRC: ", data_crc)
    return data_crc


def decode(data_input, key):
    temp = data_input[:]
    for i in range(len(data_input) - len(key) + 1):
        if temp[i] == 1:
            temp[i : i + len(key)] = xor(temp[i : i + len(key)], key)

    remainder = temp[len(data_input) - len(key) + 1 :]
    print("Remainder after decoding: ", remainder)
    return remainder


data_input = [int(x) for x in input("Enter data bits separated by space: ").split()]
key = [int(x) for x in input("Enter the key separated by space: ").split()]

encoded_data = encode(data_input, key)

encode_data_input = [
    int(x) for x in input("Enter encoded data bits separated by space: ").split()
]

if decode(encode_data_input, key) == [0] * (len(key) - 1):
    print("No error detected")
else:
    print("Error detected in transmission")
