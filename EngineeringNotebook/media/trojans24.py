
#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
claw_motor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
arm_motor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
controller_1 = Controller(PRIMARY)
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
myVariable = 0

def when_started1():
    global myVariable
    motor_1.spin(FORWARD)
    motor_2.spin(FORWARD)
    motor_3.spin(FORWARD)
    motor_4.spin(FORWARD)
    while True:
        motor_1.set_velocity((controller_1.axis3.position() - (controller_1.axis4.position() + controller_1.axis1.position())), PERCENT)
        motor_2.set_velocity((controller_1.axis3.position() + (controller_1.axis4.position() - controller_1.axis1.position())), PERCENT)
        motor_3.set_velocity((controller_1.axis3.position() - (controller_1.axis4.position() - controller_1.axis1.position())), PERCENT)
        motor_4.set_velocity((controller_1.axis3.position() + (controller_1.axis4.position() + controller_1.axis1.position())), PERCENT)
        arm_motor5.set_velocity(35, PERCENT)
        if controller_1.buttonL1.pressing():
            arm_motor5.spin(FORWARD)
        elif controller_1.buttonL2.pressing():
            arm_motor5.spin(REVERSE)
        else:
            arm_motor5.stop()

        if controller_1.buttonR1.pressing():
            motor_scoop6.spin(FORWARD)
        elif controller_1.buttonR2.pressing():
            motor_scoop6.spin(REVERSE)
        else:
            motor_scoop6.stop()
        wait(5, MSEC)



when_started1()
