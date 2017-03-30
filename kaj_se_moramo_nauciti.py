#Leds
l=ev3.Leds()
l.set_color(group, color) 
#group je lahko l.LEFT ali l.RIGHT
#color je lahko l.RED, l.GREEN, l.YELLOW, l.ORANGE ali l.AMBER
l.set(group, brightness_pct=0.5, trigger='timer') #nastavimo svetlost na 50% in vklopimo utripanje
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
s=ev3.Screen()
s.clear()
s.draw.lik(argumenti) #draw uporablja PIL knjižnico (glej dokumentacijo)
from PIL import Image
picture = Image.open('slika')
s.image.paste(picture, (0,0))
s.update()