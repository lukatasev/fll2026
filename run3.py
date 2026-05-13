from robot import *

def run3():
     left_att = Motor(Port.F)
     right_att = Motor(Port.B)
     right_att.control.limits(speed=500, acceleration=1000, torque=1000)
     robot.use_gyro(True)
     
     robot.straight(700)
     robot.turn(53)
     left_att.run_until_stalled(300)
     
     #right_att.run_angle(300,240)
     right_att.control.limits(speed=500, acceleration=1000, torque=100)
     right_att.run_until_stalled(300)
     right_att.control.limits(speed=500, acceleration=1000, torque=1000)

     robot.straight(220)
     right_att.run_angle(150,-280)
     wait(1000)
     right_att.run_angle(150, 280)
     robot.straight(-140)
     right_att.run_angle(300, -280)
     left_att.run_angle(300, -360)
     robot.turn(30)
     robot.settings(straight_speed=500)
     robot.straight(550)
     robot.settings(straight_speed=300)
     left_att.run_angle(300, 180)
     robot.turn(30)
     robot.straight(160)
     right_att.run_angle(300, 200)
     robot.straight(-100)  
     left_att.run_angle(300, -160)  
     robot.turn(-23)
     robot.straight(580)
     left_att.run_angle(300, 230)
     robot.turn(1)

     robot.straight(-300)
     left_att.run_angle(300,-230)
     robot.straight(180)
     robot.turn(70)
     robot.settings(straight_speed=500)
     robot.straight(750)

if __name__ == "__main__":
     run3()
