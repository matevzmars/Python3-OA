#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import time,sleep
from random import randint

s=ev3.Screen()
t1=time()
sneg=10

s.clear()

s.draw.rectangle((59,107,79,127),fill='black')
s.draw.polygon((19,107,59,97,29,97,59,87,39,87,59,77,
				49,77,69,57,89,77,79,77,99,87,79,87,
				109,97,79,97,119,107,79,107),
				fill='black')
s.update()
				
koor=[[randint(0,178),randint(0,128)] for i in range(sneg)]

while(time-t1<120):
	s.draw.point(koor)
	s.update()
	for i in range(len(koor)):
		if(koor[i][1]==127):
			koor[i][1]=randint(0,128)
			koor[i][0]=randint(0,178)
		else:
			koor[i][1]=koor[i][1]+1
	sleep(1)