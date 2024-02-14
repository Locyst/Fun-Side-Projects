def encode(string):
    encoded = []

    for word in string:
        for character in word:
            if character == " ":
                encoded.append("%20")
            elif character == "+":
                encoded.append("%40")
            else:
                encoded.append(character)
                encoded.append("+")

    return ''.join(encoded)

def decode(string):
    decoded = []
    i = 0

    while i < len(string):
        if string[i:i+3] == "%20":
            decoded.append(" ")
            i += 3
        elif string[i:i+3] == "%40":
            decoded.append("+")
            i += 3
        else:
            decoded.append(string[i])
            i += 1

    return ''.join(decoded)


print(encode("Hello World!"))
string = encode("Hello World!")
print(decode(string))
