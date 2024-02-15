import secrets


# Things to do
# Add more security

falseSpace = '​'
def reverse(string):
    """
    Returns a reversed string

    Parameters:
    - string (string): The string that will be reversed

    Returns:
    string: A reversed string of the parameter, string.
    """
    returnString = ''

    for word in string:
        for character in word:
            returnString = character + returnString

    return returnString


def generateSeed(securityLevel=10):
    """
    Creates a seed used for encoding

    Parameters:
     - securityLevel (int): The higher the number the stronger the
     seed is. Do not input decimals ( Default is 1 )

    Returns:
     - List: A list that has where the captials are, how far back
     to go, how far forwards to go and an extra
    """
    capitals = 0
    backs = 0
    fronts = 0
    extra = 0

    highest = 9 * securityLevel

    while capitals == backs or capitals == fronts or capitals == extra or capitals == 0:
        capitals = secrets.randbelow(highest)
    while backs == capitals or backs == fronts or backs == extra or backs == 0:
        backs = secrets.randbelow(highest)
    while fronts == capitals or fronts == backs or fronts == extra or fronts == 0:
        fronts = secrets.randbelow(highest)
    while extra == capitals or extra == backs or extra == fronts or extra == 0:
        extra = secrets.randbelow(highest)

    return [capitals, backs, fronts, extra]


def encode(string, seed=None):
    """
    Encodes a string using a custom encryption method

    Paramaters:
     - string (Str): The string going through the encryption method
     - seed (List[int]): The seed being used for encryption

    Return:
     - Str: The encoded string
    """
    if seed is None:
        seed = generateSeed()
        print(f'Creating encoded message using seed: {seed}')
    encoded = []
    capitals = []

    encoded.append(falseSpace)
    i = seed[0]

    while i < len(string):
        capitals.append(i)
        i += seed[0]

    i += seed[0]
    for word in string:
        for character in word:
            if character == " ":
                encoded.append(f"%{seed[3]}")
                encoded.append(falseSpace)
            else:
                char = str(ord(character.upper()) - seed[1] + seed[2])
                encoded.append(char.upper()) if i in capitals else encoded.append(char)
                encoded.append(falseSpace)
        i += 1

    return reverse(''.join(encoded))


def decode(string, seed):
    """
    Decodes a string using a custom encryption method

    Parameters:
     - string (Str): The string being decoded
     - seed (List[int]): The seed using during the encryption

    Returns:
     - Str: The decoded string
    """
    if seed is None:
        print("Cannot run without a seed")
    string = reverse(string)
    list = string.split(falseSpace)
    decoded = []
    capitals = []

    while ("" in list):
        list.remove("")

    i = seed[0]

    while i < len(list):
        capitals.append(i)
        i += seed[0]

    i = seed[0]
    for character in list:
        if "%" in character:
            if "%" in character and character == f"%{seed[3]}":
                decoded.append(" ")
        else:
            char = chr(int(character) + seed[1] - seed[2])
            decoded.append(char.lower()) if i in capitals else decoded.append(char)
        i += 1

    return ''.join(decoded)

#seed = generateSeed(50)
seed = [1, 1, 1, 1]
string = "Hello World!"

encoded = encode(string, seed)
decoded = decode(encoded, seed)

print(seed)
print(encoded)
print(decoded)
