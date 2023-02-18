#!/usr/bin/env python3

"""
This test is used to collect data from the ultrasonic sensor.
It must be run on the robot.
"""

from utils import sound
from utils.brick import TouchSensor, EV3UltrasonicSensor, wait_ready_sensors, reset_brick
from time import sleep

DELAY_SEC = 0.01  # seconds of delay between measurements
US_SENSOR_DATA_FILE = "../data_analysis/us_sensor.csv"
pitch =["Bb7","A#6","G#8","D#5"]
print("Program start.\nWaiting for sensors to turn on...")
TOUCH_SENSOR = TouchSensor(1)
US_SENSOR = EV3UltrasonicSensor(2)
Motor = Motor()
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
                if value is not None :
                    if (value > 40):
                        Motor.run_forever(speed_sp=1000)
                    sound.Sound(duration=0.3,pitch=pitch[int(value//10)],volume=100).play()
                sleep (DELAY_SEC)
    except BaseException:
        print ("Done with the program")
        reset_brick()
        exit()


if __name__ == "__main__":
    continuous_sound_touch_sensor()

