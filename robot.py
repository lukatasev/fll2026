from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task

# Drive base
hub = PrimeHub()
left_drive = Motor(Port.E, positive_direction=Direction.COUNTERCLOCKWISE)
right_drive = Motor(Port.A)

robot = DriveBase(
    left_drive,
    right_drive,
    wheel_diameter=56,
    axle_track=128
)

# Attachment motors
#left_att = Motor(Port.F)
#right_att = Motor(Port.B)
