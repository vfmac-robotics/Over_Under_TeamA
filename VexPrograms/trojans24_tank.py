
#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
motor_rb = Motor(Ports.PORT10, GearSetting.RATIO_18_1,False)
motor_lt = Motor(Ports.PORT3, GearSetting.RATIO_18_1,True)
motor_rt = Motor(Ports.PORT20, GearSetting.RATIO_18_1,False)
motor_lb = Motor(Ports.PORT11, GearSetting.RATIO_18_1,True)
motor_in = Motor(Ports.PORT2)
motor_blooket = Motor(Ports.PORT13)




controller_1 = Controller(PRIMARY)

motor_in.set_velocity(100,PERCENT)
#motor_scoop6.set_velocity(25,PERCENT)

# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration
robot_direction = -1
speed_scaler = 0.8

#motor_rb.set_reversed(True)
#motor_lt.set_reversed(False)
#motor_rt.set_reversed(True)
#motor_lb.set_reversed(False)

def when_started1():
    global robot_direction
    motor_rb.spin(REVERSE)
    motor_lt.spin(FORWARD)
    motor_rt.spin(REVERSE)
    motor_lb.spin(FORWARD)

    while True:

       #motor_rb.set_velocity(robot_direction*(controller_1.axis3.position() + robot_direction*(controller_1.axis1.position())), PERCENT)
       #motor_lt.set_velocity(robot_direction*(controller_1.axis3.position() - robot_direction*(controller_1.axis1.position())), PERCENT)
       #motor_rt.set_velocity(robot_direction*(controller_1.axis3.position() + robot_direction*(controller_1.axis1.position())), PERCENT)
       #motor_lb.set_velocity(robot_direction*(controller_1.axis3.position() - robot_direction*(controller_1.axis1.position())), PERCENT)
        
        motor_rb.set_velocity(speed_scaler*robot_direction*(controller_1.axis3.position() - robot_direction*(controller_1.axis1.position())), PERCENT)
        motor_lt.set_velocity(speed_scaler*robot_direction*(controller_1.axis3.position() + robot_direction*(controller_1.axis1.position())), PERCENT)
        motor_rt.set_velocity(speed_scaler*robot_direction*(controller_1.axis3.position() - robot_direction*(controller_1.axis1.position())), PERCENT)
        motor_lb.set_velocity(speed_scaler*robot_direction*(controller_1.axis3.position() + robot_direction*(controller_1.axis1.position())), PERCENT)
       
        if controller_1.buttonR1.pressing():
            motor_in.spin(REVERSE)
        elif controller_1.buttonL1.pressing():
            motor_in.spin(FORWARD)
        else:
            motor_in.stop()

        if controller_1.buttonR2.pressing():
            motor_blooket.spin(FORWARD)
        elif controller_1.buttonL2.pressing():
            motor_blooket.spin(REVERSE)
        else:
            motor_blooket.stop()
        wait(5, MSEC)

def robot_orientation():
    global robot_direction
    robot_direction = robot_direction*-1

def speed_scaler_inc():
    global speed_scaler
    speed_scaler = speed_scaler + 0.05
    if speed_scaler > 100:
        speed_scaler = 100
   
def speed_scaler_dec():
    global speed_scaler
    speed_scaler = speed_scaler - 0.05
    if speed_scaler < 0:
        speed_scaler = 0

controller_1.buttonA.pressed(robot_orientation)
controller_1.buttonUp.pressed(speed_scaler_inc)
controller_1.buttonDown.pressed(speed_scaler_dec)


def pre_autonomous ():
    wait(1, SECONDS)

def autonomous():
    auto_off_side()

def user_control():
    while True:
        wait (20, MSEC)
        when_started1()

comp = Competition(user_control, autonomous)
pre_autonomous()
