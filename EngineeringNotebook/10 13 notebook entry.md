Since our _holonomic_ code from lat year only had four motors programmed, we had to create a brand new code using some of the VEX Sample code. We are now able to fully operate our robot to its maximum capacity. One basic change that we made was adjust the velocity of the _scooper_ to 25% from the default 30%. Our thinking was that we needed to stress contact towards our triballs using the rubber flaps to make it work better.

#### Code:
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



https://github.com/vfmac-robotics/Over_Under_TeamA/assets/145074938/7b0002a9-3656-4d77-83f1-ed4110ef2d96


#### Upgrades to be done upcoming:
* Add hooks to the circled area and try and elevate the robot using the scooper's arm motor.


   <img src="media/hookidea.jpeg" width="350" height="400">
* figure out if we can add another motor to try and ease the strain on the single motor 
* Replace the front C channel from a 35 to a 25
* stabilize the scoop

  <img src="media/ideaforstability.jpeg" width="350" height="400">
  
  We're thinking by leaving a little bit of space to let one triball edge go thru, we can get a better grip on the triball.
#### Solution to fit the 18x18x18 restriction
* Shorten the chasis supports on the arm from a 35 to either a 30 or 25
* make the claw a 35 c channel to be able to get matchloads. 


