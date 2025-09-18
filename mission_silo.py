from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

# Set up all devices.
prime_hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
left_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.B, Direction.CLOCKWISE)
drive_base = DriveBase(left_wheel, right_wheel, wheel_diameter=63, axle_track=136)
claw = Motor(Port.F, Direction.COUNTERCLOCKWISE, gears=[12, 20])
fork = Motor(Port.E, Direction.COUNTERCLOCKWISE, gears=[12, 20])

drive_base.use_gyro(True)
drive_base.settings(straight_speed=500, turn_rate=100)


# ## mission
claw.run_target(100, 100)
fork.run_target(100, 20)

drive_base.straight(400)
drive_base.turn(-45)
drive_base.straight(155)
drive_base.turn(90)
drive_base.straight(-140)
drive_base.straight(200)
drive_base.turn(-45)
drive_base.straight(150)
drive_base.turn(75)
drive_base.straight(-90)
fork.run_target(100, -28)
drive_base.turn(-30)
drive_base. straight(-30)
drive_base. turn(-30)
drive_base. turn(20)
fork.run_target(100, 20)
drive_base.turn(-80)
drive_base. straight(250)
drive_base. turn(-45)
drive_base. straight(90)
drive_base. turn(-30)
drive_base. straight(155)
drive_base. turn(30)
claw.run_target(100, -5)
drive_base. straight(450)
claw.run_target(100, 80)
drive_base. turn()



# claw.run_target(100, 5)
# drive_base.straight(200)
# drive_base.straight(-200)



