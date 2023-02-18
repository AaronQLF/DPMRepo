from utils.brick import EV3GyroSensor, wait_ready_sensors, TouchSensor,reset_brick
gyro_sensor = EV3GyroSensor(4)
gyro_sensor.reset_angle()

while True: 
    print (gyro_sensor.get_value()