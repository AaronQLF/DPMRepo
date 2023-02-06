#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor


COLOR_SENSOR_DATA_FILE = "../data_analysis/color_sensor.csv"

# complete this based on your hardware setup
_ = EV3ColorSensor(2)
_ = TouchSensor(1)

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


def collect_color_sensor_data():
    file = open(COLOR_SENSOR_DATA_FILE, "w")
    file.write("color\n")
    try:
        while True:
            if (TOUCH_SENSOR.is_pressed()):
                file.write(str(COLOR_SENSOR.get_color()) + "\n")
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        file.close()
        exit()

if __name__ == "__main__":
    collect_color_sensor_data()
