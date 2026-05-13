from robot import *

def run1():
    leftm  = Motor(Port.F, positive_direction=Direction.CLOCKWISE, gears=[12, 20, 36], reset_angle=True)
    leftm.control.limits(speed=200, acceleration=1000, torque=500)
    rightm = Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=[12, 24], reset_angle=True)
    rightm.control.limits(speed=500, acceleration=1000, torque=100)
    robot.use_gyro(True)

    leftm.run_until_stalled(200)
    leftm.run_angle(100, -80, wait=False)
    rightm.run_until_stalled(-100)
    rightm.control.limits(speed=200, acceleration=1000, torque=500)
    robot.straight(650)
    robot.straight(-100)
    wait(250)
    robot.straight(50)
    leftm.run_angle(100, 68)
    robot.straight(-100)
    leftm.run_angle(100, -40)

    robot.straight(290)
    robot.turn(-40)
    rightm.run_angle(100, 160)
    robot.straight(70)
    rightm.run_angle(100, -40)
    robot.turn(-7)
    robot.straight(100)
    robot.turn(5)

    robot.straight(-145)
    robot.turn(10)
    robot.straight(55)
    rightm.run_angle(100, -60)
    robot.settings(straight_speed=500, turn_rate=180)
    robot.turn(30)
    robot.straight(-1000)


if __name__ == "__main__":
    run1()
