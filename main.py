from robot import *
from run1 import *
from run2 import *
from run3 import *
from run4 import *
from run5 import *
from run6 import *
from newrun import *
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task

runs = {
    1: run1,
    2: run2,
    3: run3,
    4: run4,
    5: run5,
    6: run6,
    7: newrun
}

current_run = 1
pressed = []

hub.system.set_stop_button(Button.BLUETOOTH)
while True:
    was_pressed = pressed
    pressed = hub.buttons.pressed()
    hub.display.number(current_run)

    if Button.LEFT in pressed and Button.LEFT not in was_pressed:
        current_run -= 1
        hub.display.number(current_run)
    elif Button.RIGHT in pressed and Button.RIGHT not in was_pressed:
        current_run += 1
        hub.display.number(current_run)
    elif Button.CENTER in pressed and Button.CENTER not in was_pressed:
        runs[current_run]()

    wait(50)
