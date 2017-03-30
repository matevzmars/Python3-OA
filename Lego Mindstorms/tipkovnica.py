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

mB=ev3.LargeMotor('outA')
mC=ev3.LargeMotor('outB')

mB.duty_cycle_sp=0
mC.duty_cycle_sp=0

mB.run_direct()
mC.run_direct()

print('...Zacetek...')

while True:
	key=readchar.readkey()
	if(key=='q' or key==ESC or key==chr(127)):
		break	
	elif(key>=chr(48) and key<=chr(57)):
		sp=10*(int(key)+1)
	elif(key==' ' or key==chr(32)):
		mB.duty_cycle_sp=0
		mC.duty_cycle_sp=0
		print('Stop')
	elif(key=='w' or key==UP):
		mB.duty_cycle_sp=sp
		mC.duty_cycle_sp=sp
		print('Naprej')
	elif(key=='s' or key==DOWN):
		mB.duty_cycle_sp=-sp
		mC.duty_cycle_sp=-sp
		print('Nazaj')
	elif(key=='a' or key==LEFT):
		mC.duty_cycle_sp=sp
		mB.duty_cycle_sp=0
		print('Levo')
	elif(key=='d' or key==RIGHT):
		mB.duty_cycle_sp=sp
		mC.duty_cycle_sp=0
		print('Desno')
	else:
		print('Ne razumem ukaza!'+key)

print('...Konec...')
mB.stop()
mC.stop()

