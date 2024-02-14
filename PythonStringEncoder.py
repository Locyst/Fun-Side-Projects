import random

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
          elif character == "+":
              encoded.append("%40")
          else:
              encoded.append(character)
              encoded.append("+")

  return ''.join(encoded)

def decode(string, seed):
  if seed is None:
    print("Cannot run without a seed")
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
        if string[i] != "+":
          decoded.append(string[i])
          i += 1
        else:
          i += 1
  
  return ''.join(decoded)

seed = createSeed()

string = encode("Hello World!", seed)
print(string)
print(decode(string, seed))
