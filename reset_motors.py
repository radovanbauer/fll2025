from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

claw = Motor(Port.F, Direction.COUNTERCLOCKWISE, gears=[12, 20])
fork = Motor(Port.E, Direction.COUNTERCLOCKWISE, gears=[12, 20])

claw.reset_angle(0)
fork.reset_angle(0)