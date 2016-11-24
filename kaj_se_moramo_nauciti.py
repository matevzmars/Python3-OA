# 7. naloga: WHILE zanka
# Dva štejeta, s tem, da eden začne pri 15, drugi pa 30. Prvi bo
# nehal štet, ko pride do 25, drugi pa 45. Ko eden neha štet, neha tudi drugi.
# Pri katerih številkah se bosta ustavila? Izpiši štetje.
# ###############################################################
# Risanje: Turtle
# import turtle
# t=turtle.Pen()
# t.forward()
# t.backward()
# t.left()
# t.right()
# t.up()
# t.down()
# t.reset()
# t.clear()
# ###############################################################
# 8. naloga: turtle
# Nariši pravokotnik, trikotnik, kvadrat brez vogalov. Kako lahko še narišeš
# kvadrat brez vogalov? Nariši hišo, ki ima vrata in dve okni. Nariši svoje ime.
# ###############################################################

#Srednji motor
m=ev3.MediumMotor('outA')

#Senzor za dotik
t=ev3.TouchSensor('in1')
a=t.is_pressed() 	# ali smo pritisnili gumb

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