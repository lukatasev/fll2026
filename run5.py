from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from robot import *

hub = PrimeHub()
def run5():
    leftm  = Motor(Port.F, positive_direction=Direction.CLOCKWISE, gears=[12, 20, 36], reset_angle=True)
    leftm.control.limits(speed=200, acceleration=1000, torque=500)
    rightm = Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=[12, 24], reset_angle=True)
    rightm.control.limits(speed=600, acceleration=1000, torque=500)
    robot.use_gyro(True)

    robot.straight(330)
    robot.turn(-4)
    for x in range(5):
        rightm.run_angle(600, 180)
        rightm.run_angle(600, -180)

    robot.settings(straight_speed=500)
    robot.straight(-500)



if __name__ == "__main__":
    run5()
