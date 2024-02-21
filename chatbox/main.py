import json
from difflib import get_close_matches

# From a youtube video
# Comments are being used to help me understand code

def loadKnowledge(filePath):
  """
  Loads the data base with all of the bots information

  Paramaters:
   - filePath (str): The file path where the json file is located

  Returns:
   - (dict): A dictorny with every question and their answers
  """
  with open(filePath, 'r') as file: # Opens the file at filePath
    #and stores it as file variable
    data = json.load(file) # Uses the json library to read store
    #it as a dict

  return data

def saveKnowledge(filePath, data):
  """
  Saves all of the bots information into a json file
  
  Paramaters:
   - filePath (str): The file path where the json file is located
   - data (str): The data that is being stored
  """
  with open(filePath, "w") as file: # Opens the file at filePath 
    #and stores it as a variable
    json.dump(data, file, indent=2) # Uses the json library to 
    #dump the knowledge dict to store it inside of the file

def findBestMatch(userQuestion, questions, cutoff=0.6):
  """
  Locates the best match for the question in the knowledge database

  Parameters:
   - userQuestion (str): The question that the user asked
   - questions (dict): The dictorniaty that stores every question and their answers
   - cutoff (float): How precise does the match have to do be

  Returns:
   - Union[str, None]: Returns the best match if there is one otherwise it returns nothing
  
  """
  matches = get_close_matches(userQuestion, questions, n=1, cutoff=cutoff) # Uses the get_close_matches function in the 
  #difflib library to find the question in the dict that best 
  #matches the userQuestion
  return matches if matches else None

def getAnswerForQuestion(question, knowledgeData):
  """
  Returns the stored answer for the question given

  Parameters:
   - question (str): The question that the user asked
   - knowledgeData (str): The whole database of questions and 
   their answers

  Returns:
   - str: The answer to said question
  """
  for q in knowledgeData["questions"]:
    if q["questions"] == question:
      return q["answer"]

def chatBot():
  knowledge = loadKnowledge('knowledge.json')

  while True:

    userInput = input("You: ")

    if userInput.lower() == 'quit':
      break

    bestMatch = findBestMatch(userInput, [q['questions'] for q in knowledge['questions']])
    
    if bestMatch:
      answer = getAnswerForQuestion(bestMatch[0], knowledge)
      print(f'Bot: {answer}')
    else:
      print("Bot: dunno, tell me how I should respond? (skip to skip)")
      newAnswer = input('You: ')

      if newAnswer.lower() != 'skip':
        knowledge['questions'].append({"questions": userInput, "answer": newAnswer})
        saveKnowledge('knowledge.json', knowledge)

if __name__ == '__main__':
  chatBot()
