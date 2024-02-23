class LocystStatistics:
    @classmethod
    def organize(cls, inputList):
        return sorted(inputList)
    
    @classmethod
    def oddCheck(cls, num):
        if num % 2 == 0:
            return False
        else:
            return True
    
    @classmethod
    def meanCalculate(cls, inputList): # Average
      inputList = cls.organize(inputList)
      mean = 0
    
      for num in inputList:
        mean += num
    
      mean = mean / len(inputList)
      
      return mean
      
    @classmethod
    def modeCalculate(cls, inputList): # Most Common
      inputList = cls.organize(inputList)
    
      return max(set(inputList), key=inputList.count)
      
    @classmethod
    def medianCalculate(cls, inputList): # Middle
      inputList = cls.organize(inputList)
    
      if cls.oddCheck(len(inputList)):
          while len(inputList) > 1:
              del inputList[0]
              del inputList[-1]
          return inputList[0]
      else:
          while len(inputList) > 2:
              del inputList[0]
              del inputList[-1]
          return (((inputList[-1] - inputList[0]) / 2) + inputList[0])
      return "I dunno the logic yet"
      
    @classmethod
    def rangeCalculate(cls, inputList): # Biggest - Smallest
      inputList = cls.organize(inputList)
      lowest = inputList[0]
      highest = inputList[-1]
    
      Range = highest - lowest
    
      return Range
  
  
  
def test(inputList = [1, 5, 2, 3, 6, 7, 3]):
    print(f'inputList: {inputList}\n')
    
    print(f'The mean is: {LocystStatistics.meanCalculate(inputList)}')
    print(f'The mode is: {LocystStatistics.modeCalculate(inputList)}')
    print(f'The median is: {LocystStatistics.medianCalculate(inputList)}')
    print(f'The range is: {LocystStatistics.rangeCalculate(inputList)}')
    
if __name__ == '__main__':
    test()
