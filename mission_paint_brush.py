from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

# Set up all devices.
prime_hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
left_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.B, Direction.CLOCKWISE)
drive_base = DriveBase(left_wheel, right_wheel, wheel_diameter=63, axle_track=136)
fork = Motor(Port.E, Direction.COUNTERCLOCKWISE, gears=[12, 20])

drive_base.use_gyro(True)
drive_base.settings(straight_speed=500, turn_rate=100)


# ## mission
fork.run_target(100, 50)
drive_base.straight(670)
fork.run_target(100,-40)
drive_base.turn(-20)
drive_base.straight(60)
# pushed one of the topsoil
drive_base.straight(-60)
fork.run_target(100, -15)
drive_base.turn(18)
drive_base.straight(-10)
drive_base.straight(55)

fork.run_target(100, 50)

drive_base.turn(5)
drive_base.straight(-50)
drive_base.turn(-3)
drive_base.straight(-250)
drive_base.turn(90)
fork.run_target(100, -40)
drive_base.turn(-90)
drive_base.straight(-450)
drive_base 