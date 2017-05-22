#!/usr/bin/env python3
import ev3dev.ev3 as ev3

s=ev3.Sound()

s.play_song((('D4', 'e3'),('D4', 'e3'),
                 ('D4', 'e3'),('G4', 'h'),
                 ('D5', 'h'),('C5', 'e3'),
                 ('B4', 'e3'),('A4', 'e3'),
                 ('G5', 'h'),('D5', 'q'),
                 ('C5', 'e3'),('B4', 'e3'),
                 ('A4', 'e3'),('G5', 'h'),
                 ('D5', 'q'),('C5', 'e3'),
                 ('B4', 'e3'),('C5', 'e3'),
                 ('A4', 'h.'),),tempo=120,delay=50).wait()

				
print('...Konec...')