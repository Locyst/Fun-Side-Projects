# ---------- Logic Gates ---------- #

class LocystGates:
  def __init__(self, inputType=None):
      """
      Parameters:
       - inputType: List of input type values, default is [1, 0]. The first value is the True value with the second one being the False one
      """
      if inputType is None:
        inputType = [1, 0]
      self.inputType = inputType

  def _variableCheck(self, *args):
      """
      Checks the variables inputted in the arguements to make sure that theyre valid inputs

      Parameters:
       - arg1: The first input value
       - arg2: The second input value

      Returns:
       - Returns the objects True or False value based on whether the inputs are valid ones
      """
      returnState = self.inputType[0]
      for variable in args:
          if variable not in self.inputType:
              returnState = self.inputType[1]

      if returnState:
          return self.inputType[0]
      else:
          print("Arguements have to be a int")
          return self.inputType[1]

  def AND(self, arg1: int, arg2: int) -> int:
      """
      Logical AND operation between two input values

      Parameters:
       - arg1: The first input value
       - arg2: The second input value

      Returns:
       - int: Output value based on the logical AND operation
      """
      if self._variableCheck(arg1, arg2) != self.inputType[0]:
          return self.inputType[1]

      return self.inputType[0] if (arg1 == arg2) else self.inputType[1]

  def OR(self, arg1: int, arg2: int) -> int:
      """
      Logical OR operation between two input values

      Parameters:
       - arg1: The first input value
       - arg2: The second input value

      Returns:
       - int: Output value based on the logical OR operation
      """
      if self._variableCheck(arg1, arg2) != self.inputType[0]:
          return self.inputType[1]

      return self.inputType[0] if (arg1 == self.inputType[0]) or (arg2 == self.inputType[0]) else self.inputType[1]

  def XOR(self, arg1: int, arg2: int) -> int:
      """
      Logical XOR operation between two input values

      Parameters:
       - arg1: The first input value
       - arg2: The second input value

      Returns:
       - int: Output value based on the logical XOR operation
      """
      if self._variableCheck(arg1, arg2) != self.inputType[0]:
          return self.inputType[1]

      if (arg1 != self.inputType[0]) and (arg2 != self.inputType[0]):
          return self.inputType[1]

      if (arg1 == arg2):
          return self.inputType[1]

      return self.inputType[0]

  def NOT(self, arg1: int) -> int:
      """
      Logical NOT operation for the input value

      Parameters:
       - arg1: The input value to perform NOT operation on

      Returns:
       - int: Output value based on the logical NOT operation
      """
      if not self._variableCheck(arg1):
          return self.inputType[1]

      return self.inputType[0] if (arg1 == self.inputType[1]) else self.inputType[1]

  def NOR(self, arg1: int, arg2: int) -> int:
      """
      Logical NOR operation between two input values

      Parameters:
       - arg1: The first input value
       - arg2: The second input value

      Returns:
       - int: Output value based on the logical NOR operation
      """
      if self._variableCheck(arg1, arg2) != self.inputType[0]:
          return self.inputType[1]

      return self.NOT(self.OR(arg1, arg2))
