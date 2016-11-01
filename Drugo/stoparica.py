from time import time,sleep
from tkinter import *
import winsound as w

def stoparica():
    b=Button(tk,text='Začni',width=10,command=zacni,font=('Times',15))
    b.pack(side='left')
    b=Button(tk,text='Ustavi',width=10,command=ustavi,font=('Times',15))
    b.pack(side='left')

def zacni():
    global run
    run=True
    return stej()

def stej():    
    t=time()
    while run:
        c.delete('all')
        c.create_text(500,200,text=('%.3f' % (time()-t)),font=('Times',100))
        c.update()
    
def ustavi():
    global run
    run=False
    return 0

def odstevalnik():
    l=Label(tk,text='Vnesi čas (v sekundah):')
    l.pack(side='right')
    e=Entry(tk,bd=5)
    e.pack(side='right')
    e.focus_set()
    b=Button(tk,text='Ustavi',width=10,command=ustavi,font=('Times',15))
    b.pack(side='right')
    def ods():
        global run
        run=True
        return odstej(int(e.get()))
    b=Button(tk,text='Ok',width=10,command=ods,font=('Times',15))
    b.pack(side='right')

def odstej(x):
    w.Beep(800,500)
    sleep(1)
    w.Beep(800,500)
    sleep(1)
    w.Beep(800,500)
    sleep(1)
    w.Beep(1200,500)
    t=time()
    while time()-t<x and run:
        c.delete('all')
        c.create_text(500,200,text=('%.3f' % (x-time()+t)),font=('Times',100))
        c.update()
    c.delete('all')
    c.create_text(500,200,text=('0.000'),font=('Times',100))
    for i in range(3):
        w.Beep(1200,100)

tk=Tk()
c=Canvas(tk,width=1000,height=400)
b=Button(tk,text='Štoparica',width=10,command=stoparica,font=('Times',15))
b.pack(side='left')
b=Button(tk,text='Odštevalnik',width=10,command=odstevalnik,font=('Times',15))
b.pack(side='right')
c.pack()
