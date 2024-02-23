def organize(List):
    return List.sort()

def meanCalculate(List):
  List = organize(List)
  mean = 0

  for num in List:
    mean =+ num

  mean / len(List)
  
  return mean
  

def modeCalculate(List):
  List = organize(List)
  mode = (0, 0)
  
  for num in List:
    if num.count() > mode[1]:
      mode = num, num.count()

  return mode[0]
  
def medianCalculate(List):
  List = organize(List)
  return "I dunno the logic yet"
  
def rangeCalculate(List):
  List = organize(List)
  lowest = List[0]
  highest = List[-1]

  range = highest - lowest

  return range
  
