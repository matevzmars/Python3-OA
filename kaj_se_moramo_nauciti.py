#Barvni senzor
c=ev3.ColorSensor('in2')
a=c.ambient_light_intensity() 	#intenziteta okoliške svetlobe
b=c.blue() 	#koliko modre barve smo zaznali
r=c.red() 	#koliko rdeče barve smo zaznali
g=c.green() 	#koliko zelene barve smo zaznali
d=c.color() 	#kakšno svetlobo smo zaznali (glej dokumentacijo)
e=c.reflected_light_intensity() 	#intenziteta odbite svetlobe

#Senzor razdalje
u=ev3.UltrasonicSensor('in3')
a=u.distance_centimeters()	#pove razdaljo
b=u.other_sensor_present()	#preveri ali sliši se kakšen ultrazvočni senzor

#Žiroskop
g=ev3.GyroSensor('in4')
a=g.angle() #vrne kot
b=g.rate()	#vrne kotno hitrost

#Tipke
b=ev3.Button()
a=b.backspace()	#preveri ali je pritisnjen gumb nazaj
a=b.down()		#preveri ali je pritisnjen gumb dol
a=b.enter()		#preveri ali je pritisnjen gumb enter
a=b.up()		#preveri ali je pritisnjen gumb gor
a=b.left()		#preveri ali je pritisnjen gumb levo
a=b.right()		#preveri ali je pritisnjen gumb desno

#Led

#Zaslon

#Zvok