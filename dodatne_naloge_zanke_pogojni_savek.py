1. naloga:
Izpiši števila, ki so deljiva s 7 in so večkratniki števila 5, med 
števili 1500 in 2700.

REŠITEV:
for i in range(1500,2701):
	if(i%7==0 and i%5==0):
		print(i)
		
DRUGA MOŽNA REŠITEV:
a=1500
while(a<=2700):
	if(i%7==0 and i%5==0):
		print(i)

2. naloga:
Napiši program, v katerem uporabnik ugiba število med 1 in 100. 
Rešuj z metodo bisekcije. Prvi dve vrstici programa naj vsebujeta:
from random import *
a=randint(1,100)

REŠITEV:
from random import *
a=randint(1,100)
b=0

while(b!=a):
	b=input('Vpiši številko: ')
	b=int(b)
	if(b<1 or b>100):
		print('Število je zunaj okvirjev, poskusi znova!')
	elif(b>a):
		print('Število je preveliko. Poskusi znova!')
	elif(b<a):
		print('Število je premajhno. Poskusi znova!')
		
print('Uganil si! Iskano število je: %s' %a)

3. naloga:
Napiši program, ki uporabnika vpraša po besedi in jo izpiše v obratnem
vrstnem redu. (Namig: beseda je neke vrste seznam)

4. naloga:
Napiši program, ki uporabnika vpraša po številki in izpiše vsoto vseh 
naravnih števil, da vnešene številke (vključno z njo).
Primer:
Vpiši število: 4
10
Vpiši število: 5
15
Vpiši število: 50
1275

5. naloga:
Napiši program, ki uporabnika vpraša po številki in izpiše večkratnike 
tega števila.
Primer:
Vpiši število: 6
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
...