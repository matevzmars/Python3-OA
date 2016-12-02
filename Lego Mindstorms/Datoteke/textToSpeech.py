#!/usr/bin/env python3
import ev3dev.ev3 as ev3

s=ev3.Sound()

i=''

while i!='q':
	s.speak(i).wait()
	i=input('Kaj naj izgovorim? ')

print('Finish')
