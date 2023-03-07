def encode(string):
    newstring = ''
    for x in string:
        newstring += str((int(x) + 3) % 10)
    return newstring

def decode(string):
    newstring = ''
    for x in string:
        newstring += str((int(x) - 3) % 10)
    return newstring


print(decode('123'))
