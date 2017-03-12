#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

mB = ev3.LargeMotor('outB')
mC = ev3.LargeMotor('outC') #motorja priključimo na izhoda B in C

mB.stop_action = 'brake'
mC.stop_action = 'brake' 

g = ev3.GyroSensor('in1') #žiro-senzor priklopimo na vhod 1

g.mode = 'GYRO-ANG' #žiro-senzor nastavimo v način merjenja kota

mB = run_forever(speed_sp=450) #začnemo vrteti robota
mC = run_forever(speed_sp=0)

x=0
while(abs(x)<45): #dokler je kot manjši od 45 stopinj se izvaja zanka
	x=g.value()
	sleep(0.01)
	
mB.stop()
mC.stop()
	
mB = run_to_rel_pos(speed_sp=450, position_sp=360)
mC = run_to_rel_pos(speed_sp=450, position_sp=360) #kolesa zavrtimo za en obrat