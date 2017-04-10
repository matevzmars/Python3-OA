#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from random import randint
from time import sleep

l = ev3.Leds()
b = ev3.Button()

color = [l.GREEN, l.YELLOW, l.ORANGE, l.AMBER, l.RED]

while(b.backspace):
	l.set_color(l.LEFT, color[randint(0,4)])
	l.set_color(l.RIGHT, color[randint(0,4)])
	sleep(0.1)
	
	
l.all_off()
