#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

mB = ev3.LargeMotor('outB')
mC = ev3.LargeMotor('outC') #motorja priključimo na izhoda B in C

mB.stop_action = 'brake'
mC.stop_action = 'brake' 

b = ev3.Button()

while(b.backspace):
	if(not b.up):
		mB.run_to_rel_pos(position_sp=360,speed_sp=450)
		mC.run_to_rel_pos(position_sp=360,speed_sp=450)
	if(not b.down):
		mB.run_to_rel_pos(position_sp=-360,speed_sp=450)
		mC.run_to_rel_pos(position_sp=-360,speed_sp=450)
	if(not b.left):
		mB.run_to_rel_pos(position_sp=360,speed_sp=450)
		mC.run_to_rel_pos(position_sp=0,speed_sp=450)
	if(not b.right):
		mB.run_to_rel_pos(position_sp=0,speed_sp=450)
		mC.run_to_rel_pos(position_sp=360,speed_sp=450)