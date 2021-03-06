#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

#Program s katerim se lego robot (osnovni model) premakne za dva obrata motorja naprej, počaka 1 sekundo, se premakne za 720 stopinj obrata motorja nazaj, počaka 1 sekundo in se na koncu premika 1 sekundo naprej

m1=ev3.LargeMotor('outA') #prvi motor smo povezali na A izhod
m2=ev3.LargeMotor('outB') #drugi motor smo povezali na B izhod

m1.run_to_rel_pos(position_sp=360*2,speed_sp=500, stop_action='brake') #motor 1 se premakne za dva obrata
m2.run_to_rel_pos(position_sp=360*2,speed_sp=500, stop_action='brake') #motor 2 se premakne za dva obrata

while(len(m1.state)>0 or len(m2.state)>0): #počakaj dokler se motor 1 ali motor 2 premika
	pass									#neumen ukaz

sleep(1) #počakamo 1 sekundo

m1.run_to_rel_pos(position_sp=-720,speed_sp=500, stop_action='brake') #motor 1 se premakne za 720 stopinj v drugo smer
m2.run_to_rel_pos(position_sp=-720,speed_sp=500, stop_action='brake') #motor 2 se premakne za 720 stopinj v drugo smer

while(len(m1.state)>0 or len(m2.state)>0): #počakaj dokler se motor 1 ali motor 2 premika
	pass										#neumen ukaz

sleep(1) #počakamo 1 sekundo

m1.run_timed(time_sp=1000,speed_sp=500, stop_action='brake') #motor 1 deluje 1 sekundo
m2.run_timed(time_sp=1000,speed_sp=500, stop_action='brake') #motor 2 deluje 1 sekundo

