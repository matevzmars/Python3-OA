#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

c=ev3.ColorSensor('in1')

print('Ambientalna svetloba')
for i in range(5):
	print(c.ambient_light_intensity())
	sleep(2)

print('Barva')
for i in range(5):
	print(c.color())
	sleep(2)

print('Odbita svetloba')
for i in range(5):
	print(c.reflected_light_intensity())
	sleep(2)

print('Po komponentah')
for i in range(5):
	print(c.red())
	print(c.green())
	print(c.blue())
	print(' ')
	sleep(2)

print('...Konec...')
