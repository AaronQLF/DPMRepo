
from BrickPi import *   								#import BrickPi.py file to use BrickPi operations
BrickPiSetup()  										# setup the serial port for communication
BrickPi.SensorType[PORT_4] = TYPE_SENSOR_EV3_GYRO_M0   	#Set the type of sensor at PORT_4.  M0 is angle. 
BrickPiSetupSensors()   								#Send the properties of sensors to BrickPi.  Set up the BrickPi.
# There's often a long wait for setup with the EV3 sensors.
# EV3 gyro works best (less drift and less error results) if you hold it still in setup.
while True:
	result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors 
	if not result :
		gyro =BrickPi.Sensor[PORT_4]
		print(str(gyro))
	time.sleep(.01)     # sleep for 10 ms
