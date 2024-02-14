import random

# Things to do
# Add capitals to encryption method
# Find ways to improve security

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

def createSeed(securityLevel=1):
  """
  Creates a seed used for encoding

  Parameters:
   - securityLevel (int): The higher the number the stronger the
   seed is. Do not input decimals ( Default is 1 )

  Returns:
   List: A list that has where the captials are, how far back to
   go, how far forwards to go and an extra
  """
  capitals = random.randint(0, 9 * securityLevel)
  backs = random.randint(0, 9 * securityLevel)
  fronts = random.randint(0, 9 * securityLevel)
  extra = random.randint(0, 9 * securityLevel)

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
    seed = createSeed()
    print(f'Creating encoded message using seed: {seed}')
  encoded = []

  encoded.append("+")

  for word in string:
      for character in word:
          if character == " ":
              encoded.append("%20")
              encoded.append("+")
          elif character == "+":
              encoded.append("%40")
              encoded.append("+")
          else:
              encoded.append(str(ord(character) - seed[1] + seed[2]))
              encoded.append("+")
  
  
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
  list = string.split('+')
  decoded = []

  
  while("" in list):
    list.remove("")

  for character in list:
    if "%" in character:
      match character:
        case "%20":
          decoded.append(" ")
        case "%40":
          decoded.append("+")
    else:
      decoded.append(chr(int(character) + seed [1] - seed[2]))
  
  return ''.join(decoded)

seed = createSeed(5)

string = encode("Goodbye World!", seed)
print(string)
print(decode(string, seed))
