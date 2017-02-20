Kaj že znamo:
###############################################################
Matematika
a+b
a-b
a/b
a//b
a%b
a**b
abs(a)
###############################################################
Posebni znaki
#
\'
\n
\t
###############################################################
Zajemanje
a=input('Besedilo')
###############################################################
Izpisovanje
a='Tekst'
print(a)
print(2*a)
print('Tekst %s' %a)
###############################################################
Funkcije
int()   #pretvori besedo v številko
chr()   #pretvori številko v znak
str()   #pretvori številko v besedo
print('Besedilo'+str(b))
###############################################################
Seznami
seznam=[a,b,c,d,...]        #ustvari seznam
print(seznam)               #izpiše celotni seznam
print(seznam[i])            #izpiše i-ti člen seznama
print(seznam[i:j])          #izpiše člene od i-tega do j-tega
seznam[i]=a                 #zamenja i-ti člen z vrednostjo a
del seznam[i]               #izbriše i-ti člen
seznam.append(a)            #doda nov člen a na konec seznama
seznam=[seznam1,seznam2]    #ustvari nov seznam, sestavljen iz seznama1 in seznama2
seznam=seznam1+seznam2      #ustvari nov seznam, kjer združi člene dveh seznamov
seznam=seznam1*5            #5 krat ponovi člene seznama
len(seznam)                 #vrne dolžino seznama/število členov
###############################################################
Tupli-permanentni seznami
seznam=(a,b,c,d,...)
seznam[i]=a?
###############################################################
Maps-slovarji
seznam={a:b,c:d,...}
a,c ključi, b,d vrednosti
print(seznam[a])
del seznam[a]
seznam[a]=d
###############################################################
Pogojni stavki
if(a>b):
    print(a)
elif(a==b):
    print(a+b)
else:
    print(b)
==
!=
<
>
<=
>=
or, and, oklepaji!
a, b isti podatkovni tip
###############################################################
Zanke:FOR
for i in range(0,5,2):
    print(i)
for i in seznam:
    print(i)
###############################################################
Zanke:WHILE
while a<100:
    print(a)
    a=a+1
if + break
while True:
    print(a)
###############################################################
Risanje: Turtle
import turtle
t=turtle.Pen()
t.forward()
t.backward()
t.left()
t.right()
t.up()
t.down()
t.reset()
t.clear()
t.circle(1)
###############################################################
Lego Mindstorms

http://python-ev3dev.readthedocs.io/en/latest/spec.html
https://sites.google.com/site/ev3python/

#!/usr/bin/env python3
import ev3dev.ev3 as ev3
###############################################################
Motorji
m=ev3.LargeMotor('outA')

#neskončno vrtenje
m.run_forever(speed_sp=100) #speed_sp je od 0 do 900
m.stop(stop_action='brake') #stop_action je lahko 'brake' ali 'coast'

#vrtenje za določen kot
m.run_to_rel_pos(position_sp=360,speed_sp=100) 

#neskončno vrtenje, kjer lahko vmes spreminjaš hitrost
m.run_direct(duty_cycle_sp=20) #duty_cycle je od 0 do 100
m.duty_cycle_sp=30

#vrtenje za določen čas
m.run_timed(time_sp=1000,speed_sp=100) #čas je v milisekundah

m.reset()

m.duty_cycle_sp=50
m.duty_cycle_sp

from time import sleep
sleep(5) #počaka 5 sekund

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
