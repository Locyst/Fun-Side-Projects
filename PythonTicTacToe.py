class GameScripts:
  def __init__(self):
    self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    self.boardHeight = len(self.board)
    self.boardLength = len(self.board[0])
    self.player = "X"
    self.winner = None
    self.gameOver = False
    self.moves = 0

  def printBoard(self):
    border = "  " + "+" + "-" * (self.boardLength * 2 - 1) + "+"
    print("   1 2 3")
    print(border)
    for y in range(3):
      letter = "A" if y == 0 else "B" if y == 1 else "C"
      print(f"{letter} |", end='')
      for x in range(3):
        print(self.board[y][x], end="|")
      print("\n" + border)
    print("\n\n")

  def placeMove(self, x, y):
    if self.board[y][x] == " ":
      self.board[y][x] = self.player
      self.moves += 1
      self.checkWin()
      self.switchPlayer()
    else:
      print("You can't put your piece here!")

  def checkWin(self):
    # Check horizontal
    for y in range(3):
      if self.board[y][0] == self.board[y][1] == self.board[y][2] != " ":
        self.winner = self.board[y][0]
        self.gameOver = True
    # Check vertical
    for x in range(3):
      if self.board[0][x] == self.board[1][x] == self.board[2][x] != " ":
        self.winner = self.board[0][x]
        self.gameOver = True
    # Check diagonal
    if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
      self.winner = self.board[0][0]
      self.gameOver = True
    if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
      self.winner = self.board[0][2]
      self.gameOver = True

  def switchPlayer(self):
    self.player = "X" if self.player == "O" else "O"

  def getPlayerMovement(self):
    movement=input(f"Where would you like to place your {self.player}? Example: (A1)\n> ")
    movement = [*movement]
    print(movement)
    y = 1 if movement[0] == "A" else 2 if movement[0] == "B" else 3
    x = int(movement[1])
    x = int(x) - 1
    y = int(y) - 1
    self.placeMove(x, y)

game = GameScripts()

game.printBoard()
while game.gameOver is not True:
  game.getPlayerMovement()
  game.printBoard()
print(f"{game.winner} has won in {game.moves} moves!")
