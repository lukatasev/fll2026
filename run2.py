from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from robot import *

hub = PrimeHub()

def run2():
    leftm  = Motor(Port.F, positive_direction=Direction.CLOCKWISE, gears=[12, 20, 36], reset_angle=True)
    leftm.control.limits(speed=500, acceleration=1000, torque=500)
    rightm = Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=[12, 24], reset_angle=True)
    rightm.control.limits(speed=500, acceleration=1000, torque=100)
    robot.use_gyro(True)

    leftm.run_until_stalled(300)
    rightm.run_until_stalled(-300)
    robot.straight(350)
    rightm.run_until_stalled(300)
    robot.settings(straight_speed=500, turn_rate=300)
    robot.straight(-200)
    robot.turn(-45)
    rightm.run_until_stalled(-300)
    
    robot.straight(200)
    robot.turn(50)
    robot.straight(200)
    wait(100)
    robot.turn(-8)
    robot.straight(400)
    robot.settings(straight_speed=500)
    robot.straight(-700)
    

    
    


if __name__ == "__main__":
    run2()
    
