from Notas import *
#Notas
notas=[do,mi,sol,si,re,fa,la,do]
volumen=0.2

#---------------------------

for i in range(1,len(notas)):
    if notas[i]<notas[i-1]:
        for j in range(i,len(notas)):
            notas[j]*=2.

#---------------------------
server = Server().boot()
server.start()
sine=[]
for i in range(len(notas)):
    sine.append(Sine(notas[i], mul=volumen).out())
sleep(3)
server.stop()