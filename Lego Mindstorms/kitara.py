#!/usr/bin/env python3
import ev3dev.ev3 as ev3

s=ev3.Sound()
u=ev3.UltrasonicSensor('in1')
b=ev3.Button()
t=ev3.TouchSensor('in2')
a=60

while(b.backspace):
	ton=u.distance_centimeters
	if(t.is_pressed):
		if(ton<a):
			s.play_song((('C4','q')))
		elif(ton<a*2):	
			s.play_song((('D4','q')))
		elif(ton<a*3):	
			s.play_song((('E4','q')))
		elif(ton<a*4):	
			s.play_song((('F4','q')))
		elif(ton<a*5):	
			s.play_song((('G4','q')))
		elif(ton<a*6):	
			s.play_song((('A4','q')))
		elif(ton<a*7):	
			s.play_song((('H4','q')))
			
