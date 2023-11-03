The competition is in two days. We have some doubts and concerns, but are feeling rather confident with our notebook as it was our main focus this year. 
---- -
Today our parts that we ordered came after weeks. We took the robot's upper half apart and started rewiring the whole robot. We had to specifically cut each wire for the desired length.  

### The Process:
First you had to find the size wire you needed for the robot. Then you had to cut it with the specific VEX tool. Then you had to strip the black off the wire to a certain point then you put the male connectors on and press on it with the tool to finalize the process. 

### Our Wire Lengths
* Port 1 = 30 cm
* Port 2 = 18 cm
* Port 3 = 30 cm
* Port 11 = 43 cm
* Port 10 = 30cm
* Port 21 = 6cm


Our current code for the robot
```
#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
motor_4 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
arm_motor5 = Motor(Ports.PORT10, GearSetting.RATIO_18_1,True)
motor_scoop6 = Motor(Ports.PORT11, GearSetting.RATIO_18_1,True)
controller_1 = Controller(PRIMARY)
arm_motor5.set_velocity(60,PERCENT)
motor_scoop6.set_velocity(25,PERCENT)

# wait for rotation sensor to fully initialize
wait(30, MSEC)
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
```
#### One Notable thing :
We switched the ports for motor 4 to port 21 with a significantly shorter cable.




 <img src="media/wiredbase.jpeg" width="350" height="400">
_The finished product of the base_

### The base
We made some slight adjustments to the base layout as well. For one we trimmed the X-Drive's shafts so it's not sticking too far out of the robot. 

 <img src="media/leitnercutting.jpg" width="350" height="400">
