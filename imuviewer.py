import serial
import re
from vpython import *
import math

encoding = 'utf-8'
arduino = serial.Serial('COM13', 115200, timeout=.1)
myboxpos = vector(0,0,0)
mybox = box(pos=myboxpos,size = vector(1,1,1),color=color.red)
xaxis = arrow(pos = vector(2,2,2), axis=vector(1,0,0),shaftwidth=0.1,color = color.red)
yaxis = arrow(pos = vector(2,2,2), axis=vector(0,1,0),shaftwidth=0.1,color = color.green)
zaxis = arrow(pos = vector(2,2,2), axis=vector(0,0,1),shaftwidth=0.1,color = color.blue)

prev_x = 0.0
prev_y = 0.0
prev_z = 0.0
while True:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    if data:
        datastr = data.decode(encoding)
        #print(datastr.find("X"))
        #print(datastr.find("Y"))
        #print(datastr.find("Z"))
        values = re.findall("\d+\.\d+",datastr)
        if len(values) is 3:
            print(values)
            x = math.radians(float(values[0]))
            y = math.radians(float(values[1]))
            z = math.radians(float(values[2]))
            dx = x - prev_x # Delta x
            dy = y - prev_y # Delta y
            dz = z - prev_z # Delta z
            mybox.rotate(angle=dx, axis=vector(1,0,0))
            mybox.rotate(angle=dy, axis=vector(0,1,0))
            mybox.rotate(angle=dz, axis=vector(0,0,1))
            prev_x = x
            prev_y = y
            prev_z = z

