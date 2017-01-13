#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

#Program s katerim se lego robot (osnovni model) vrti dokler ne zazna črne črte

m1=ev3.LargeMotor('outA') #prvi motor smo povezali na A izhod
m2=ev3.LargeMotor('outB') #drugi motor smo povezali na B izhod

c=ev3.ColorSensor('in1') #barvni senzor smo priklopili na vhod 1

m1.run_forever(speed_sp=500) #prvi motor se bo vrtel

while(c.reflected_light_intensity()>50): #dokler bo barvni senzor prebral vrednost odbite svetlobe več od 50 se izvaja neumna zanka
	i=0

m1.stop() #ustavimo motor 1