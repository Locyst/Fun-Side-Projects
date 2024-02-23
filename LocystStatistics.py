class LocystStatistics:
    @staticmethod
    def organize(input_list):
        """Sorts the input list."""
        return sorted(input_list)
    
    @staticmethod
    def odd_check(num):
        """Checks if a number is odd."""
        return num % 2 != 0

    @staticmethod
    def numeric_check(input_list):
        """Checks if all elements in the list are numeric."""
        return all(isinstance(x, (int, float)) for x in input_list)

    @staticmethod
    def length_check(input_list):
        """Checks if the list is not empty."""
        return len(input_list) > 0

    @classmethod
    def mean(cls, input_list):
        """Calculates the mean of the input list."""
        if not cls.numeric_check(input_list) or not cls.length_check(input_list):
            raise ValueError("Input list must contain numeric values and cannot be empty")
        
        return sum(input_list) / len(input_list)

    @classmethod
    def mode(cls, input_list):
        """Calculates the mode of the input list."""
        if not cls.numeric_check(input_list) or not cls.length_check(input_list):
            raise ValueError("Input list must contain numeric values and cannot be empty")
        
        return max(set(input_list), key=input_list.count)

    @classmethod
    def median(cls, input_list):
        """Calculates the median of the input list."""
        if not cls.numeric_check(input_list) or not cls.length_check(input_list):
            raise ValueError("Input list must contain numeric values and cannot be empty")
        
        sorted_list = cls.organize(input_list)
        n = len(sorted_list)
        if cls.odd_check(n):
            return sorted_list[n // 2]
        else:
            return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

    @classmethod
    def range(cls, input_list):
        """Calculates the range of the input list."""
        if not cls.numeric_check(input_list) or not cls.length_check(input_list):
            raise ValueError("Input list must contain numeric values and cannot be empty")
        
        sorted_list = cls.organize(input_list)
        return sorted_list[-1] - sorted_list[0]
  
  
def test(input_list=[1, 5, 2, 3, 6, 7, 3]):
    print(f'input_list: {input_list}\n')
    
    print(f'The mean is: {LocystStatistics.mean(input_list)}')
    print(f'The mode is: {LocystStatistics.mode(input_list)}')
    print(f'The median is: {LocystStatistics.median(input_list)}')
    print(f'The range is: {LocystStatistics.range(input_list)}')
    
if __name__ == '__main__':
    test()
