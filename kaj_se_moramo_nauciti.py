#Senzor razdalje
u=ev3.UltrasonicSensor('in3')
a=u.distance_centimeters	#pove razdaljo v milimetrih!
b=u.other_sensor_present	#preveri ali sliši se kakšen ultrazvočni senzor

#Tipke
b=ev3.Button()
a=b.backspace	#preveri ali je pritisnjen gumb nazaj
a=b.down		#preveri ali je pritisnjen gumb dol
a=b.enter		#preveri ali je pritisnjen gumb enter
a=b.up			#preveri ali je pritisnjen gumb gor
a=b.left		#preveri ali je pritisnjen gumb levo
a=b.right		#preveri ali je pritisnjen gumb desno
a=b.any()		#preveri ali je pritisnjen kakršenkoli gumb
a=b.buttons_pressed #vrne seznam pritisnjenih gumbov

#Leds
l=ev3.Leds()
l.set_color(group, color) 
#group je lahko LEFT ali RIGHT
#color je lahko RED, GREEN, YELLOW, ORANGE ali AMBER
l.set(group, brightness_pct=0.5, trigger='timer') #nastavimo svetlost na 50% in vklopimo utripanje
a=l.max_brightness #vrne največjo dovoljeno svetlost
l.brightness_pct=0.50 #nastavi svetlost
l.delay_on=10 #pri utripanju je LED dioda prižgana 10 milisekund
l.delay_off=20 #pri utripanju je LED dioda ugasnjena 20 milisekund
l.all_off() #izključi LED diode

#Zvok
s=ev3.Sound()
s.beep() 
s.play('ime_datoteke.wav') #predvaja zvočno datoteko
s.get_volume #vrne glasnost
s.set_volume #določi glasnost v %
s.speak('besedilo') #pretvori tekst v govor
s.tone(frekvenca, dolžina)
s.tone([(frekvenca, dolžina, pavza),...])
s.play_song(pesem, tempo=120, delay=50) #pesem je permanentni seznam permanentnih seznamov oblike (nota, dolžina), kjer je nota oblike npr. A4 in dolžina q - četrtinka, h - polovinka, e - osminka
.wait()
 
#Zaslon
s=ev3.Screen
s.clear()
s.draw.lik(argumenti) #draw uporablja PIL knjižnico (glej dokumentacijo)
from PIL import Image
picture = Image.open('slika')
s.image.paste(picture, (0,0))
s.update()