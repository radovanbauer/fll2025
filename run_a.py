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
claw.run_target(100, 75)
fork.run_target(100, 25)

drive_base.straight(400)
drive_base.turn(-45)
drive_base.straight(155)
drive_base.turn(90)
drive_base.straight(-145)
drive_base.straight(205)
drive_base.turn(-45)
drive_base.straight(150)
drive_base.turn(75)
drive_base.straight(-70)
fork.run_target(100, -22)
drive_base.turn(-30)
drive_base. straight(0)
drive_base. turn(-35)
drive_base. turn(25)
fork.run_target(100, 25)
drive_base.turn(-80)
drive_base. straight(250)
drive_base. turn(-45)
drive_base. straight(90)
drive_base. turn(-30)
drive_base. straight(73)
drive_base. turn(30)
claw.run_target(100, -4)
drive_base. straight(445)
claw.run_target(100, 55)
drive_base.straight(525)
drive_base.turn(-80)
drive_base.straight(760)




