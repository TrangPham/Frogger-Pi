import LEDGrid as LED

def hello():
  print "Hello World"

def winGameMsg(output_method):
  grid = [[0 for x in range(8)] for y in range(8)]
  grid[3][2] = 1
  grid[4][2] = 1
  grid[2][3] = 1
  grid[2][4] = 1
  grid[3][5] = 1
  grid[4][5] = 1
  grid[5][4] = 1
  grid[5][3] = 1
  if output_method == "LED":
    printLED(grid)
  else:
    printScreen(grid)
def endGameMsg(output_method):
  grid = [[0 for x in range(8)] for y in range(8)]
  grid[3][3] = 1
  grid[4][3] = 1
  grid[2][2] = 1
  grid[2][5] = 1
  grid[3][4] = 1
  grid[4][4] = 1
  grid[5][2] = 1
  grid[5][5] = 1
  if output_method == "LED":
    printLED(grid)
  else:
    printScreen(grid)
def printScreen(grid):
  for row in grid:
    print row
def printLED(grid):
  LED.setup()
  LED.on(grid)

