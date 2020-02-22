import time
import board
import busio
import adafruit_lsm6ds
from networktables import NetworkTables
from adafruit_lsm6ds import LSM6DSOX
import numpy

NetworkTables.initialize(server = 'roborio-3637-frc.local')
sd = NetworkTables.getTable("SmartDashboard")

i2c = busio.I2C(board.SCL, board.SDA)
sensor = LSM6DSOX(i2c)

i = 0

while i == 0:
#	sd.putNumber("X Angle", sensor.gyro[0])
#	sd.putNumber("Y Angle", sensor.gyro[1])
#	sd.putNumber("Z Angle", sensor.gyro[2])
#	sd.putNumber("X Accel", sensor.acceleration[0])
#	sd.putNumber("Y Accel", sensor.acceleration[1])
#	sd.putNumber("Z Accel", sensor.acceleration[2])

	z = sensor.acceleration[2]
	x = sensor.acceleration[0]
	g = numpy.sqrt(z * z + x * x)
	angle = numpy.arcsin(z / g)
	angle *= 180 / numpy.pi
	if x < 0:
		angle *= -1
	#print("The angle is ", angle)
	#print(sensor.acceleration[0], " ", sensor.acceleration[1], " ", sensor.acceleration[2])
	sd.putNumber("Angle", angle)
	time.sleep(0.05)

