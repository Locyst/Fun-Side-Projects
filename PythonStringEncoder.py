import random

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

def createSeed():
  capitals = random.randint(0, 9)
  backs = random.randint(0, 9)
  fronts = random.randint(0, 9)
  extra = random.randint(0, 9)

  return [capitals, backs, fronts, extra]

def encode(string, seed=None):
  if seed is None:
    seed = createSeed()
  encoded = []

  encoded.append("+")

  print(f'Creating encoded message using seed: {seed}')

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

seed = createSeed()

string = encode("Hello World!", seed)
print(string)
print(decode(string, seed))
