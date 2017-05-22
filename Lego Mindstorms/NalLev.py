#!/usr/bin/env python3
import ev3dev.ev3 as ev3

m=ev3.LargeMotor('outA')
t1=ev3.TouchSensor('in1')
t2=ev3.TouchSensor('in2')
b=ev3.Button()

m.stop_action='brake'

while(b.backspace):
	if(t1.is_pressed): #recmo za izstrelitev
		m.run_to_rel_pos(speed_sp=900, position_sp=360)
	if(t2.is_pressed): #za navitje
		m.run_to_rel_pos(speed_sp=100, position_sp=-360)