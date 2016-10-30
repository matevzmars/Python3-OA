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
