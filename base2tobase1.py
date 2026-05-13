from robot import *

def run4fi():
    leftm  = Motor(Port.F, positive_direction=Direction.CLOCKWISE, gears=[12, 20, 36], reset_angle=True)
    leftm.control.limits(speed=500, acceleration=1000, torque=500)
    rightm = Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=[12, 24], reset_angle=True)
    rightm.control.limits(speed=500, acceleration=1000, torque=200)
    robot.use_gyro(True)
    
    rightm.run_angle(300, -150)
    robot.settings(straight_speed=400)
    robot.straight(350)
    robot.turn(-95)
    robot.straight(1600)
    robot.turn(-90)
    robot.straight(300)







if __name__ == "__main__":
    run4fi()

