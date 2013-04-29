import RPi.GPIO as GPIO

def setup():
  GPIO.setmode(GPIO.BCM)
  #MUX
  GPIO.setup( 4, GPIO.OUT) #S1
  GPIO.setup( 3, GPIO.OUT) #S2
  GPIO.setup( 2, GPIO.OUT) #S3
  #Columns
  GPIO.setup( 17, GPIO.OUT)
  GPIO.setup( 27, GPIO.OUT)
  GPIO.setup( 22, GPIO.OUT)
  GPIO.setup( 23, GPIO.OUT)
  GPIO.setup( 24, GPIO.OUT)
  GPIO.setup( 10, GPIO.OUT)
  GPIO.setup( 9, GPIO.OUT)
  GPIO.setup( 11, GPIO.OUT)

def setRow(row):
  GPIO.output(4, row[0])
  GPIO.output(3, row[1])
  GPIO.output(2, row[2])

def setCol(col):
  GPIO.output( 17, col[0])
  GPIO.output( 27, col[1])
  GPIO.output( 22, col[2])
  GPIO.output( 23, col[3])
  GPIO.output( 24, col[4])
  GPIO.output( 10, col[5])
  GPIO.output(  9, col[6])
  GPIO.output( 11, col[7])

def setGrid(row, col):
  setCol([0,0,0,0,0,0,0,0]) #clear it so that it won't appear on the next row
  setRow(row)
  setCol(col) 
 
def on(grid):
  #currently no way to turn it off (infinate loop)
  #must loop through the rows, 
  #turning on the columns needed for that row then go to the next one
  while (True):
    setGrid([0,0,0], grid[0])
    setGrid([0,0,1], grid[1])
    setGrid([0,1,0], grid[2])
    setGrid([0,1,1], grid[3])
    setGrid([1,0,0], grid[4])
    setGrid([1,0,1], grid[5])
    setGrid([1,1,0], grid[6])
    setGrid([1,1,1], grid[7])

def off():
  print "TODO: implement method"
  #Stop flashing through the rows and outputting
  #Clear (because the GPIO pins will hold last value set)