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


fork.run_target(100, 0)
claw.run_target(100, 0)