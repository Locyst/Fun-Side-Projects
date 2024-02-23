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
        for num in inputList:
            if str(num).isnumeric() is False:
                return False
        return True

    @classmethod
    def lengthCheck(cls, inputList):
        if len(inputList) < 1:
            return False
        return True

    @classmethod
    def mean(cls, inputList): # Average
        if cls.numericCheck(inputList=inputList) and cls.lengthCheck(inputList=inputList):
            inputList = cls.organize(inputList)
            mean = 0
            
            for num in inputList:
                mean += num
                
            mean = mean / len(inputList)
            
            return mean
        else:
            if cls.numericCheck(inputList=inputList) is False:
                print("List cannot have strings")
            if cls.lengthCheck(inputList=inputList) is False:
                print("List cannot be empty")
      
    @classmethod
    def mode(cls, inputList): # Most Common
        if cls.numericCheck(inputList=inputList) and cls.lengthCheck(inputList=inputList):
            inputList = cls.organize(inputList)
            
            return max(set(inputList), key=inputList.count)
        else:
            if cls.numericCheck(inputList=inputList) is False:
                print("List cannot have strings")
            if cls.lengthCheck(inputList=inputList) is False:
                print("List cannot be empty")
      
    @classmethod
    def median(cls, inputList): # Middle
        if cls.numericCheck(inputList=inputList) and cls.lengthCheck(inputList=inputList):
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
        else:
            if cls.numericCheck(inputList=inputList) is False:
                print("List cannot have strings")
            if cls.lengthCheck(inputList=inputList) is False:
                print("List cannot be empty")

      
    @classmethod
    def range(cls, inputList): # Biggest - Smallest
        if cls.numericCheck(inputList=inputList) and cls.lengthCheck(inputList=inputList):
            inputList = cls.organize(inputList)
            lowest = inputList[0]
            highest = inputList[-1]
            
            Range = highest - lowest
            
            return Range
        else:
            if cls.numericCheck(inputList=inputList) is False:
                print("List cannot have strings")
            if cls.lengthCheck(inputList=inputList) is False:
                print("List cannot be empty")

  
  
  
def test(inputList = [1, 5, 2, 3, 6, 7, 3]):
    print(f'inputList: {inputList}\n')
    
    print(f'The mean is: {LocystStatistics.mean(inputList)}')
    print(f'The mode is: {LocystStatistics.mode(inputList)}')
    print(f'The median is: {LocystStatistics.median(inputList)}')
    print(f'The range is: {LocystStatistics.range(inputList)}')
    
if __name__ == '__main__':
    test()
