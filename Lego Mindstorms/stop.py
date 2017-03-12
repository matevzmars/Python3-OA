#!/usr/bin/env python3
import ev3dev.ev3 as ev3

mB = ev3.LargeMotor('outB')
mC = ev3.LargeMotor('outC')

mB.stop_action = 'brake'
mC.stop_action = 'brake'

mB.stop()
mC.stop()