def organize(List):
    return sorted(List)

def meanCalculate(List):
  List = organize(List)
  mean = 0

  for num in List:
    mean =+ num

  mean / len(List)
  
  return mean
  

def modeCalculate(List):
  List = organize(List)

  return max(set(List), key=List.count)
  
def medianCalculate(List):
  List = organize(List)
  return "I dunno the logic yet"
  
def rangeCalculate(List):
  List = organize(List)
  lowest = List[0]
  highest = List[-1]

  range = highest - lowest

  return range
  
  
  
def test(List = [1, 5, 2, 3, 6, 7, 3])
    print(f'List: {List}')
    
    print(f'The mean is: {meanCalculate(List)}')
    print(f'The mode is: {modeCalculate(List)}')
    print(f'The median is: {medianCalculate(List)}')
    print(f'The range is: {rangeCalculate(List)}')
    
if __name__ == '__main__':
    test()
