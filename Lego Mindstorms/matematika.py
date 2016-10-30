#!/usr/bin/env python3
from time import sleep

a=int(input('Vpisi prvo stevilko:'))
b=int(input('Vpisi drugo stevilko:'))

v=a+b
r=a-b
k=a/b
c=a//b
o=a%b

print('Vsota %s + %s je: %s' %(a,b,v)) 
print('Razlika %s - %s je: %s' %(a,b,r)) 
print('Kvocient %s / %s je: %s' %(a,b,k)) 
print('Celostevilski kvocient pri deljenju %s / %s je: %s' %(a,b,c)) 
print('Ostanek pri deljenju %s / %s je: %s' %(a,b,o))
print('\n \n \n')

sleep(5)

e=input('...pritisni ENTER za izhod...')
