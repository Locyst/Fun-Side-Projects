class LocystStatistics:
    @classmethod
    def organize(cls, List):
        return sorted(List)
    
    @classmethod
    def oddCheck(cls, num):
        if num % 2 == 0:
            return False
        else:
            return True
    
    @classmethod
    def meanCalculate(cls, List): # Average
      List = cls.organize(List)
      mean = 0
    
      for num in List:
        mean += num
    
      mean = mean / len(List)
      
      return mean
      
    @classmethod
    def modeCalculate(cls, List): # Most Common
      List = cls.organize(List)
    
      return max(set(List), key=List.count)
      
    @classmethod
    def medianCalculate(cls, List): # Middle
      List = cls.organize(List)
    
      if cls.oddCheck(len(List)):
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
      
    @classmethod
    def rangeCalculate(cls, List): # Biggest - Smallest
      List = cls.organize(List)
      lowest = List[0]
      highest = List[-1]
    
      Range = highest - lowest
    
      return Range
  
  
  
def test(List = [1, 5, 2, 3, 6, 7, 3]):
    print(f'List: {List}\n')
    
    print(f'The mean is: {LocystStatistics.meanCalculate(List)}')
    print(f'The mode is: {LocystStatistics.modeCalculate(List)}')
    print(f'The median is: {LocystStatistics.medianCalculate(List)}')
    print(f'The range is: {LocystStatistics.rangeCalculate(List)}')
    
if __name__ == '__main__':
    test()
