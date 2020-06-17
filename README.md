# IMU_3DViewer
Python client to visualize absolute orientation from a BNO055 by means of an Arduino Nano with Adafruit libraries

## Details

It read from the the serial port connected to an Arduino Nano. The Arduino
Nano has been burned with the Examples/Adafruit BNO055/sensorapi sketch.
The sketch sends over the serial port the absolute orientation in the form of:
<code>
X: 328.8750 Y: 3.1875 Z: -1.0000  
</code> 
Values are in degrees

## Environment
Windows 10
Anaconda

## Dependencies
Python 3
pyserial (pip install pyserial)
vpython (pip install vpython) [vpython.org]
