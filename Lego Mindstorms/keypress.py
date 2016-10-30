#!/usr/bin/env python3
import readchar

UP='\x1b\x5b\x41'
DOWN='\x1b\x5b\x42'
RIGHT='\x1b\x5b\x43'
LEFT='\x1b\x5b\x44'
ESC='\x1b\x1b'

while True:
	key=readchar.readkey()
	if key==ESC or key=='q' or key==chr(127):
		print('Pritisnil si q ali ESC')
		break
	elif key=='w' or key==UP:
		print('Pritisnil si gor')
	elif key=='a' or key==LEFT:
		print('Pritisnil si levo')
	elif key=='s' or key==DOWN:
		print('Pritisnil si dol')
	elif key=='d' or key==RIGHT:
		print('Pritisnil si desno')
	elif key==chr(13):
		print('Pritisnil si ENTER')
	else:
		print(ord(key))
