#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

mA=ev3.LargeMotor('outA')
mB=ev3.LargeMotor('outB')

kot=int(input('Vpisi kot: '))

mB=run_to_rel_pos(speed_sp=100, position_sp=kot)

sleep(5)

mA=run_to_rel_pos(speed_sp=900, position_sp=100)
sleep(5)
mA=run_to_rel_pos(speed_sp=900, position_sp=-100)
