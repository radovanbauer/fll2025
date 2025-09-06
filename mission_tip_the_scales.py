from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

# Set up all devices.
prime_hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
left_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.B, Direction.CLOCKWISE)
drive_base = DriveBase(left_wheel, right_wheel, wheel_diameter=63, axle_track=136)
claw = Motor(Port.F, Direction.COUNTERCLOCKWISE)
fork = Motor(Port.E, Direction.COUNTERCLOCKWISE)

drive_base.use_gyro(True)
drive_base.settings(straight_speed=1000, turn_rate=100)


# mission
claw.run_target(100, 170)
fork.run_target(100, 150)
drive_base.straight(450)
drive_base.turn(-90)
drive_base.straight(230)
drive_base.turn(90)
drive_base.straight(470)
drive_base.turn(-90)
drive_base.straight(217)
drive_base.turn(90)
drive_base.straight(35)
fork.run_target(100, -10)
fork.run_target(100, 150)
drive_base.turn(90)
drive_base.straight(315)
drive_base.turn(-90)
drive_base.straight(60)
drive_base.turn(-90)
claw.run_target(100, -10)
drive_base.straight(-80)
drive_base.turn(-45)
drive_base.straight(200)
drive_base.turn(-25)
drive_base.straight(40)
claw.run_target(100, 170)
drive_base.turn(-20)
drive_base.straight(300)
drive_base.turn(-25)
drive_base.straight(500)
claw.run_target(100, -10)
