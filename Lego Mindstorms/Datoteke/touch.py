#!/usr/bin/env python3
import ev3dev.ev3 as ev3


t=ev3.TouchSensor('in1')

print('Pritisni gumb!')

while(t.is_pressed()!=1):
	i=1

print('...Konec...')
