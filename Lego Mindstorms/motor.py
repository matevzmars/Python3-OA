#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep


m=ev3.LargeMotor('outA')
n=ev3.LargeMotor('outB')

m.run_forever(speed_sp=100)
n.run_forever(speed_sp=100)

sleep(5)

#m.stop(stop_action='brake')
#n.stop(stop_action='coast')
m.stop()
n.stop()


m.run_timed(time_sp=1000, speed_sp=100)
n.run_timed(time_sp=1000, speed_sp=100)
