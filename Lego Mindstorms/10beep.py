#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

s=ev3.Sound()

for i in range(10):
	s.beep()
	sleep(0.2)
	print(i+1)

print('...Konec...')
