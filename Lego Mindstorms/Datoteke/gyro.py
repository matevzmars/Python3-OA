#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

g=ev3.GyroSensor('in1')

print('Kot')
for i in range(10):
	print(g.angle())
	sleep(1)
print('Kotna hitrost')
for i in range(10):
	print(g.rate())
	sleep(1)

print('...Konec...')
