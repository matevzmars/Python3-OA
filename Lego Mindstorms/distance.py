#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

dist=ev3.UltrasonicSensor('in2')
t=ev3.TouchSensor('in1')

while(t.is_pressed()!=1):
	print(dist.distance_centimeters()) #to je v milimetrih
	sleep(1)

print('...Konec...')

