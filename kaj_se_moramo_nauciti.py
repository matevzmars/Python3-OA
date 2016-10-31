# 7. naloga: WHILE zanka
# Dva štejeta, s tem, da eden začne pri 15, drugi pa 30. Prvi bo
# nehal štet, ko pride do 25, drugi pa 45. Ko eden neha štet, neha tudi drugi.
# Pri katerih številkah se bosta ustavila? Izpiši štetje.
# ###############################################################
# Risanje: Turtle
# import turtle
# t=turtle.Pen()
# t.forward()
# t.backward()
# t.left()
# t.right()
# t.up()
# t.down()
# t.reset()
# t.clear()
# ###############################################################
# 8. naloga: turtle
# Nariši pravokotnik, trikotnik, kvadrat brez vogalov. Kako lahko še narišeš
# kvadrat brez vogalov? Nariši hišo, ki ima vrata in dve okni. Nariši svoje ime.
# ###############################################################
# http://python-ev3dev.readthedocs.io/en/latest/spec.html
# https://sites.google.com/site/ev3python/

# #!/usr/bin/env python3
# import ev3dev.ev3 as ev3
# ###############################################################
# Motorji
# m=ev3.LargeMotor('outA')

# #neskončno vrtenje
# m.run_forever(speed_sp=100) #speed_sp je od 0 do 900
# m.stop(stop_action='brake') #stop_action je lahko 'brake' ali 'coast'

# #vrtenje za določen kot
# m.run_to_rel_pos(position_sp=360,speed_sp=100) 

# #neskončno vrtenje, kjer lahko vmes spreminjaš hitrost
# m.run_direct(duty_cycle_sp=20) #duty_cycle je od 0 do 100
# m.duty_cycle_sp=30

# #vrtenje za določen čas
# m.run_timed(time_sp=1000,speed_sp=100) #čas je v milisekundah

# m.reset()

# m.duty_cycle_sp=50
# m.duty_cycle_sp

# from time import sleep
# sleep(5) #počaka 5 sekund

