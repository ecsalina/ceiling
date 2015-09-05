import serial
import random

ser = serial.Serial("COM3", 9600)
numLEDs = 18
rows = 7
cols = 5
colorSep = ','
LEDsep = ';'
fullStop = '.'




#FUNCTION CALLS
LEDBuffer = randomColors()
write(LEDBuffer)




#CLASSES:
class LED(object):
	__init__(self, c):
		self.R = c[0]
		self.G = c[1]
		self.B = c[2]

grid = [[LED((255, 255, 255)) for j in range(cols)] for i in range(rows)]
delete = True
for i in range(rows):
	for j in range(cols):
		if delete:
			grid[i][j] = None
			delete != delete



#WRITE FUNCTIONS:
def write(*args):
	for arg in args:
		writeHelper(arg)

def writeHelper(data):
	line = ""
	for i,LED in enumerate(data):
		line.append(str(i))
		line.append(colorSep)
		for c in LED:
			line.append(str(c))
			line.append(colorSep)
		line = line[:-1]
		line.append(LEDsep)
	line = line[:-1]
	line.append(fullStop)







#COLOR FUNCTIONS:
def writeColor(grid, x, y, c):
	"""
	Takes a grid and changes one color
	"""
	grid = grid[:]
	grid[x][y] = c

def sameColor(grid, c):
	"""
	Sets each LED to the same given color.
	"""
	grid = grid[:]
	for x in range(rows):
		for y in range(cols):
			if grid[x][y] != None:
				grid[x][y] = c


	for i in range(numLEDs):
		LEDBuffer.append(color)
	return LEDBuffer




def randomColors():
	"""
	Sets a random color to each LED in array.
	"""
	LEDBuffer = []
	for i in range(numLEDs):
		r = random.random()*255
		g = random.random()*255
		b = random.random()*255
	LEDBuffer.append((r, g, b))
	return LEDBuffer


def fade(buff1, buff2, frames=10):
	"""
	Given two LED buffers, this will fade between them. Takes optional argument
	frames which determines how many intermediate buffers to produce (i.e., how
	how long the fade is), including the original and final buffers.
	"""
	frames -= 1

	buffer = [[0, 0, 0] for i in range(numLEDs)]
	LEDBuffers = [buffer for i in range(frames+1)]

	for i in range(numLEDs):
		R1 = buff1[i][0]
		G1 = buff1[i][1]
		B1 = buff1[i][2]

		R2 = buff2[i][0]
		G2 = buff2[i][1]
		B2 = buff2[i][2]

		Rstep = (R2-R1)/frames
		Gstep = (G2-G1)/frames
		Bstep = (B2-B1)/frames

		for j in range(frames+1):
			R = R1 + j*Rstep
			G = G1 + j*Gstep
			B = B1 + j*Bstep

			LEDBuffers[j][i][0] = R
			LEDBuffers[j][i][1] = G
			LEDBuffers[j][i][2] = B

		return LEDBuffers


def load(c1, c2, ):
	"""
	Produces a progress-bar-esque effect, along one row or column, either from
	left to right or vice versa. Takes one color and transforms to a second.
	"""