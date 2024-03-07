def open_madlib_file(path="madlibs.txt"):
  def process_data(data):
    data = data.split("\n")
    return data
  with open(path, "r") as file:
      data = file.read()

  data = process_data(data)
  if len(data) == 0:
    print("No madlibs found")
    return None

  return data

def get_random_madlib(madlibs):
  import random

  return random.choice(madlibs)

def change_words(madlib):
  words = []
  madlib = madlib.split(" ")
  for word in madlib.copy():
    if word[0] == '[' and word[-1] == ']':
      word = word[1:-1]
      word = input(f"Enter a {word}: ")
      words.append(word)
    else:
      words.append(word)
  return ' '.join(words)
