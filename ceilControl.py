import serial
import random

"""
Author: Eric Salina
9/6/2015
License: MIT

This code is used to control the pattern of LEDS on the ceiling of my dorm. It
works by sending the Arduino a series RGB values to a specific LEDS (each at a
unique index) over serial. The Arduino then maps these indexes to three separate
pins for each R, G, and B, value. In the python code, each LED is assigned a
location in the double array "grid." This is based on the actual location of
of the LED on the ceiling, where each square of the waffle is one unit, and the
origin is the top left.

Animations in the code are represented as a series of slightly differing grids,
each of which are written to the Arduino over serial, in order. To have a slower
animation, more grids are added in between the initial and final grids. The
'frame-rate' of the LED refresh is 0.5 seconds. This method is more ideal over
writing to each pin individually, as it is less confusing to view the animation
as slices over time, rather than individual LEDs which are changing, each with
different delays (for example, what happens when two LEDs each fade from one
color to another in 1 second, but they do it with a different number of
intermediate steps, and therefore must be written to at different intervals?
That is a pain in the butt).

I currently don't have enough LED's/pins to fill the entire grid, so I currently
have it set up in a checkerboard fashion:
 _ _ _ _ _
|X|_|X|_|X|
|_|X|_|X|_|
|X|_|X|_|X|
|_|X|_|X|_|
|X|_|X|_|X|
|_|X|_|X|_|
|X|_|X|_|X|
"""



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


#WRITE FUNCTIONS:
def write(*args):
	for arg in args:
		writeHelper(arg)

def writeHelper(data):
	line = ""
	for x in range(rows):
		for y in range(cols):
			index = y*cols + x
			line.append(str(index))
			line.append(colorSep)
			for c in deata[x][y]:
				line.append(str(c))
				line.append(colorSep)
			line = line[:-1]
			line.append(LEDsep)
	line = line[:-1]
	line.append(fullStop)

	ser.write(line)





#COLOR FUNCTIONS:
def setColor(grid, x, y, c):
	"""
	Takes a grid and changes one color
	"""
	grid = grid[:]
	grid[x][y] = c
	return grid

def sameColor(grid, c):
	"""
	Sets each LED to the same given color.
	"""
	grid = grid[:]
	for x in range(rows):
		for y in range(cols):
			if grid[x][y] != None:
				grid = setColor(grid, x, y, c)
	return grid


def randomColors(grid):
	"""
	Sets a random color to each LED in array.
	"""
	grid = grid[:]
	for x in range(rows):
		for y in range(cols):
			if grid[x][y] != None:
				R = random.random()*255
				G = random.random()*255
				B = random.random()*255
				grid = setColor(grid, x, y, (R, G, B))
	return grid


def fade(grid1, grid2, frames=10):
	"""
	Given two LED buffers, this will fade between them. Takes optional argument
	frames which determines how many intermediate buffers to produce (i.e., how
	how long the fade is), excluding the original and final buffers.
	"""
	grid1 = grid1[:]
	grid2 = grid2[:]
	frames += 2
	grids = [grid1 for i in range(frames)]

	for x in range(cols):
		for y in range(rows):
			if grid1[x][y] != None:
				R1 = grid1[x][y][0]
				G1 = grid1[x][y][1]
				B1 = grid1[x][y][2]

				R1 = grid2[x][y][0]
				G1 = grid2[x][y][1]
				B1 = grid2[x][y][2]

				Rstep = (R2-R1)/(frames-1)
				Gstep = (G2-G1)/(frames-1)
				Bstep = (B2-B1)/(frames-1)

				for i in range(frames):
					R = R1 + i*Rstep
					G = G1 + i*Gstep
					B = B1 + i*Bstep

					grid = setColor(grid, x, y, (R, G, B))
					grids[i] = grid
	return grids


def load(grid1, grid2, index, horizontal=True, leftStart=True, topStart=True):
	"""
	Produces a progress-bar-esque effect, along one row or column, either from
	left to right or vice versa. Takes a grid and transforms to a second.

	If want to go from all one color, to another, then set grid1 to a solid
	color, and grid2 to a solid color (such as with sameColor()).
	"""
	grid1 = grid1[:]
	grid2 = grid2[:]
	grids = []
	if horizontal:
		if leftStart:
			indexes = range(cols)
		elif not leftStart:
			indexes = range(cols).reverse()

		for x in indexes:
			if grid1[x][index] != None:
				grid1[x][index] == grid2[x][index]
				newGrid = grid1[:]
				grids.append(newGrid)
		return grids

	elif not horizontal:
		if topStart:
			indexes = range(rows)
		elif not topStart:
			indexes = range(rows).reverse()

		for y in indexes:
			if grid1[index][y] != None:
				grid1[index][y] == grid2[index][y]
				newGrid = grid1[:]
				grids.append(newGrid)
		return grids

def zigzag(grid1, grid2, horizontal=True, leftStart=True, topStart=True):
	"""
	Produces a zigzag effect, based on the load function. Take one grid, and a
	secondary grid to transform them to.

	For a simple color1->color2, then input two grids of solid, different, colors.
	"""
	grid1 = grid1[:]
	grid2 = grid2[:]
	grids = []

	if horizontal:
		if topStart:
			indexes = range(rows)
		elif not topStart:
			indexes = range(rows).reverse()

		newGrid = grid1[:]
		for y in indexes:
			newGrid = load(newGrid, grid2, y, horizontal=horizontal, leftStart=leftStart)
			leftStart != leftStart
			grids.append(newGrid)

		return grids

	elif not horizontal:
		if leftStart:
			indexes = range(cols)
		elif not leftStart:
			indexes = range(cols).reverse()

		newGrid = grid1[:]
		for x in indexes:
			newGrid = load(newGrid, grid2, x, horizontal=horizontal, topStart=topStart)
			topStart != topStart
			grids.append(newGrid)

		return grids

def circle(grid1, grid2, center=(2,3), xRad=2, yRad=3):
	"""
	Draws a circle (more like rectangle) with given center and radii.
	Radii do not include the center point.
	"""
	grid1 = grid1[:]
	grid2 = grid2[:]

	x0 = center[0]
	y0 = center[1]

	topLeft = (x0-xRad, y0-yRad)
	topRight = (x0+xRad, y0-yRad)
	bottomRight = (x0+xRad, y0+yRad)
	bottomLeft = (x0-xRad, y0+yRad)

	for x in range(topLeft[0], topRight[0]):
		if grid1[x][topLeft][1] != None:
			grid1[x][topLeft][1] = grid2[x][topLeft][1]
			newGrid = grid1[:]
			grids.append(newGrid)

	for x in range(bottomLeft[0]+1, bottomRight[0])+1):
		if grid1[x][bottomLeft][1] != None:
			grid1[x][bottomLeft][1] = grid2[x][bottomLeft][1]
			newGrid = grid1[:]
			grids.append(newGrid)

	for y in range(topLeft[1]+1, bottomLeft[1]+1):
		if grid1[topLeft][0][y] != None:
			grid1[topLeft][0][y] = grid2[topLeft[0][y]
			newGrid = grid1[:]
			grids.append(newGrid)

	for y in range(topRight[1], bottomRight[1]):
		if grid1[topRight][0][y] != None:
			grid1[topRight][0][y] = grid2[topRight][0][y]
			newGrid = grid1[:]
			grids.append(newGrid)