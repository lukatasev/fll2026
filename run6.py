from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from robot import *

hub = PrimeHub()

def run6():
    leftm  = Motor(Port.F, positive_direction=Direction.CLOCKWISE, gears=[12, 20, 36], reset_angle=True)
    leftm.control.limits(speed=200, acceleration=1000, torque=500)
    rightm = Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=[12, 24], reset_angle=True)
    rightm.control.limits(speed=600, acceleration=1000, torque=100)
    robot.use_gyro(True)
    rightm.run_until_stalled(-300)
    robot.straight(50)
    robot.turn(-40)
    robot.straight(450)
    rightm.run_until_stalled(300)

    rightm.control.limits(speed=600, acceleration=1000, torque=300)
    rightm.run_angle(300, -15)
    robot.settings(straight_speed=500)
    robot.straight(-130)
    wait(200)
    robot.straight(10)
    robot.turn(8)
    rightm.run_angle(300, -10)
    robot.straight(-600)
    robot.straight(10)
    rightm.run_angle(300, -200)
    robot.straight(-800)


if __name__ == "__main__":
    run6()

