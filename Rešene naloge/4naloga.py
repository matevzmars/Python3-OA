a=input('Vpiši starost')
a=int(a)

if(a<=1):
    print('Dojenček')
elif(a<=14):
    print('Otrok')
elif(a<=19):
    print('Najstnik')
elif(a<=30):
    print('Mladostnik')
elif(a<=55):
    print('Odrasel človek')
elif(a<=120):
    print('Starček')
else:
    print('Mrtev')
