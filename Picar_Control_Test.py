from picar import front_wheels
from picar import back_wheels

import time
import picar

picar.setup()

calibrate = False
forward_speed = 80
backward_speed = 70
turning_angle = 40

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

fw.ready()
bw.ready()
fw.turning_max = 45

def straight_run():
    while True:
        bw.speed = 70
        bw.forward()
        fw.turn_straight()

def setup():
    if calibrate:
        cali()
        bw.stop()
        fw.turn(90)

def main()