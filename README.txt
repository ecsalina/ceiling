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