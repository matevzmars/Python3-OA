#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

s=ev3.Sound()

for i in range(1,11):
	s.beep()
	sleep(0.2)
	print(i)

sleep(1)
print('Finish')
