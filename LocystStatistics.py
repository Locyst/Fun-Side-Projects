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
    def numericCheck(cls, inputList):
        returnStatement = True
        for num in inputList:
            if num.isnumeric() is false:
                returnStatement = False
        return returnStatement

    def lengthCheck(cls, inputList):
        returnStatement = True
        if len(inputList) < 1:
            returnStatement = False
        return returnStatement

    @classmethod
    def meanCalculate(cls, inputList): # Average
        if cls.numericCheck(inputList) or cls.lengthCheck(inputList):
            inputList = cls.organize(inputList)
            mean = 0
            
            for num in inputList:
                mean += num
                
            mean = mean / len(inputList)
            
            return mean
        else:
            if cls.numericCheck(inputList) is False:
                print("List cannot have strings")
            if cls.lengthCheck(inputList) is false:
                print("List cannot be empty")
      
    @classmethod
    def modeCalculate(cls, inputList): # Most Common
        if cls.numericCheck(inputList) or cls.lengthCheck(inputList):
            inputList = cls.organize(inputList)
            
            return max(set(inputList), key=inputList.count)
        else:
            if cls.numericCheck(inputList) is False:
                print("List cannot have strings")
            if cls.lengthCheck(inputList) is false:
                print("List cannot be empty")
      
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
