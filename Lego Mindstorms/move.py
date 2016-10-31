#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import readchar
from time import sleep

ESC='\x1b\x1b'
UP='\x1b\x5b\x41'
DOWN='\x1b\x5b\x42'
LEFT='\x1b\x5b\x44'
RIGHT='\x1b\x5b\x43'
sp=10

m1=ev3.LargeMotor('outA')
m2=ev3.LargeMotor('outB')

m1.time_sp=1000
m2.time_sp=1000

m1.duty_cycle_sp=0
m2.duty_cycle_sp=0

m1.run_direct()
m2.run_direct()

print('...Zacetek...')

while True:
	key=readchar.readkey()
	if(key=='q' or key==ESC or key==chr(127)):
		break	
	elif(key>=chr(48) and key<=chr(57)):
		sp=10*(int(key)+1)
	elif(key==' ' or key==chr(32)):
		m1.duty_cycle_sp=0
		m2.duty_cycle_sp=0
		print('Stop')
	elif(key=='w' or key==UP):
		m1.duty_cycle_sp=sp
		m2.duty_cycle_sp=sp
		print('Naprej')
	elif(key=='s' or key==DOWN):
		m1.duty_cycle_sp=-sp
		m2.duty_cycle_sp=-sp
		print('Nazaj')
	elif(key=='a' or key==LEFT):
		m2.duty_cycle_sp=sp
		m1.duty_cycle_sp=0
		print('Levo')
	elif(key=='d' or key==RIGHT):
		m1.duty_cycle_sp=sp
		m2.duty_cycle_sp=0
		print('Desno')
	else:
		print('Ne razumem ukaza!'+key)

print('...Konec...')
m1.stop()
m2.stop()
sleep(1)

