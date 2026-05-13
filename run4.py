from robot import *

def run4():
    leftm  = Motor(Port.F, positive_direction=Direction.CLOCKWISE, gears=[12, 20, 36], reset_angle=True)
    leftm.control.limits(speed=200, acceleration=1000, torque=500)
    rightm = Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=[12, 24], reset_angle=True)
    rightm.control.limits(speed=500, acceleration=1000, torque=100)
    robot.use_gyro(True)

    
    leftm.run_until_stalled(300)
    robot.straight(300)
    rightm.run_until_stalled(-700)
    rightm.control.limits(speed=500, acceleration=1000, torque=300)
    robot.turn(-60)
    rightm.run_angle(500,150)
    robot.straight(165)
    robot.turn(-28)
    # roboto go obrkja znameto u ovaj del

    rightm.run_angle(300, -10)
    robot.straight(180)
    rightm.control.limits(speed=500, acceleration=1000, torque=100)
    rightm.run_until_stalled(500)
    robot.settings(turn_rate=300)
    robot.turn(-100)
    #izvlekuva go delo

    # vrakjanjeto na roboto nazad
    robot.straight(60)
    robot.turn(-50)
    robot.settings(straight_speed=500)
    robot.straight(700)

if __name__ == "__main__":
    run4()
