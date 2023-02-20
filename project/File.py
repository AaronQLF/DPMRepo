#!/usr/bin/env python3

"""
This test is used to collect data from the ultrasonic sensor.
It must be run on the robot.
"""

from utils import sound
from utils.brick import TouchSensor, EV3UltrasonicSensor, wait_ready_sensors, reset_brick,Motor
from time import sleep

DELAY_SEC = 0.5  # seconds of delay between measurements
pitch =["G1","A1","G8","D5"]
print("Program start.\nWaiting for sensors to turn on...")
TOUCH_SENSOR = TouchSensor(1)
EmergencyTouchSensor = TouchSensor(4)
US_SENSOR = EV3UltrasonicSensor(2)
Motor = Motor("D")
wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
print("Done waiting.")

def continuous_sound_touch_sensor():
    try :
        while (1):
            while not TOUCH_SENSOR.is_pressed():
                pass
            print ("Touch Sensor pressed")
            sleep (1)
            while (1):
                value = US_SENSOR.get_value()
                #Checks whether the touch sensor is pressed
                while not EmergencyTouchSensor.is_pressed():
                    Motor.set_power(0)
                    print("Emergency Stop")
                    exit()
                while not TOUCH_SENSOR.is_pressed():
                    value = US_SENSOR.get_value()
                    if value is not none: # if None is givenm, then data collection failed that time
                        print(value)
                        if (value < 40):
                            sound.Sound(pitch[value//10]).play()
                        else :
                            Motor.set_power(30)           
                sleep (DELAY_SEC)
    except BaseException:
        print ("Done with the program")
        reset_brick()
        exit()


if __name__ == "__main__":
    continuous_sound_touch_sensor()

