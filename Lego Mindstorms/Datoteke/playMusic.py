#!/usr/bin/env python3
import ev3dev.ev3 as ev3

s=ev3.Sound()

s.play('your_father.wav').wait()

print('...Konec...')
