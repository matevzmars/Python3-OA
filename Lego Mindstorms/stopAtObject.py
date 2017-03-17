#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

mB = ev3.LargeMotor('outB')
mC = ev3.LargeMotor('outC') #motorja priključimo na izhoda B in C

mB.stop_action = 'brake'
mC.stop_action = 'brake' 

u = ev3.UltrasonicSensor('in1') #ultrasonični senzor priklopimo na vhod 1

mB.run_forever(speed_sp=450)
mC.run_forever(speed_sp=450)

zacetna = vmesna = u.distance_centimeters
while(vmesna>zacetna-110):
	vmesna = u.distance_centimeters
	
mB.stop()
mC.stop()

sleep(1)

mB.run_forever(speed_sp=-450)
mC.run_forever(speed_sp=-450)

zacetna = vmesna = u.distance_centimeters
while(vmesna<zacetna+60):
	vmesna = u.distance_centimeters
	
mB.stop()
mC.stop()