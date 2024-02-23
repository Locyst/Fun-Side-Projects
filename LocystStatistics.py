def organize(List):
    return sorted(List)

def oddCheck(num):
    if num % 2 == 0:
        return False
    else:
        return True

def meanCalculate(List): # Average
  List = organize(List)
  mean = 0

  for num in List:
    mean += num

  mean = mean / len(List)
  
  return mean
  

def modeCalculate(List): # Most Common
  List = organize(List)

  return max(set(List), key=List.count)
  
def medianCalculate(List): # Middle
  List = organize(List)

  if oddCheck(len(List)):
      while len(List) > 1:
          del List[0]
          del List[-1]
      return List[0]
  else:
      while len(List) > 2:
          del List[0]
          del List[-1]
      return (((List[-1] - List[0]) / 2) + List[0])
  return "I dunno the logic yet"
  
def rangeCalculate(List): # Biggest - Smallest
  List = organize(List)
  lowest = List[0]
  highest = List[-1]

  range = highest - lowest

  return range
  
  
  
def test(List = [1, 5, 2, 3, 6, 7, 3]):
    print(f'List: {List}\n')
    
    print(f'The mean is: {meanCalculate(List)}')
    print(f'The mode is: {modeCalculate(List)}')
    print(f'The median is: {medianCalculate(List)}')
    print(f'The range is: {rangeCalculate(List)}')
    
if __name__ == '__main__':
    test()
