#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

#screen resolution 178x128

s=ev3.Screen()

s.draw.rectangle((50,50,100,80), fill='black')
s.update()
sleep(2)
s.clear()
s.update()
sleep(1)
s.draw.text((10,10),'Pozdravljen!')
s.update()
sleep(2)
s.clear()
s.update()

print('...Konec...')
