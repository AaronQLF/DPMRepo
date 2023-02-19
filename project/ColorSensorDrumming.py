#!/usr/bin/env python3

"""
This test is used to collect data from the ultrasonic sensor.
It must be run on the robot.
"""

from utils import sound
from utils.brick import TouchSensor, EV3UltrasonicSensor, wait_ready_sensors, reset_brick,Motor,EV3ColorSensor
from time import sleep

DELAY_SEC = 0.5  # seconds of delay between measurements
pitch =["Bb7","A#6","G#8","D#5"]
print("Program start.\nWaiting for sensors to turn on...")
TOUCH_SENSOR = TouchSensor(1)
ColorSensor = EV3ColorSensor(2)

EmergencyTouchSensor = TouchSensor(4)
Motor = Motor("D")
wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
print("Done waiting.")

def continuous_sound_touch_sensor():
    try :
        while (1):
            while (1):
                value = ColorSensor.get_value()
                #Checks whether the touch sensor is pressed
                print("Color: ", ColorSensor.get_color_name)
                if (EmergencyTouchSensor.is_pressed() == True):
                    print("Emergency Stop")
                    Motor.set_power(0)
                    break
                    sleep (DELAY_SEC)
    except BaseException:
        print ("Done with the program")
        reset_brick()
        exit()


if __name__ == "__main__":
    continuous_sound_touch_sensor()

