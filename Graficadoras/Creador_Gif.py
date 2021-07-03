# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 18:12:28 2020

@author: Alejandro Mata Ali
"""
import numpy as np
import matplotlib.pyplot as plt
from Notas import *
#--------------------------------
'''
Gráfica
q=1 Gráfica energías
q=2 Gráfica en tiempo real
q=3 Sonido
'''

q=2

#Modo inicial
modo=1

#Modalidad
modalidad=1
#---------------------------------
#Parametros
alfa=1
a=1
npmax=32
#--------------------------------
#Para música
notas=[do,mi,sol,si]
volbase=1.
velocidad=4.
#-------------------------------
#Forma de hacer el nombre del archivo
name='C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Programas\\Datos\\FPUT\\N'+str(npmax)+'\\datos_alpha'

if alfa<1. and alfa>=0.1:
    aux='{:.2f}'.format(alfa)
    name=name+'_'+aux[2:]
elif alfa<0.1 and alfa!=0:
    aux='{:.3f}'.format(alfa)
    name=name+'_0'+aux[3:]
elif alfa==0:
    name=name+'_0'
else:
    name=name+str(alfa)
    
if a<1. and a>=0.1:
    aux='{:.2f}'.format(a)
    name=name+'_a_'+aux[2:]
elif a<0.1:
    aux='{:.3f}'.format(a)
    name=name+'_a_0'+aux[3:]
else:
    name=name+'_a'+str(a)

if modalidad==1:
    name=name+'mod'+str(modo)
elif modalidad==2:
    name=name+'suma'+str(modo)+'_'+str(modo+1)
elif modalidad==3:
    name=name+'kink'
elif modalidad==4:
    name=name+'esp'

name=name+'.dat'
#--------------------------------

#Recogida datos
f = open (name,'r')
b=f.read()
f.close()

aux=b.split('\n')

npmax+=2
del b
t=[]
x=range(0, int(npmax))
u=[]
E=[]

E_1=[]
E_2=[]
E_3=[]
E_4=[]

cambio=npmax*2+1
k=int((len(aux))/cambio)#Si descomentas, añade un -1 al lado de len(aux)
'''
omega12pi=2.*np.sin(np.pi/(2.*(npmax-1)))/(2.*np.pi)

for i in range(k):
    t.append(float(aux[i*cambio])*omega12pi)
    for j in range(npmax):
        u.append(float(aux[i*cambio+1+j]))
        E.append(float(aux[i*cambio+1+npmax+j]))
'''
for i in range(k):
    t.append(float(aux[i]))
    
for i in range(k,k*npmax+k):
    u.append(float(aux[i]))
for i in range(k*npmax+k,2*k*npmax+k):
    E.append(float(aux[i]))

#Liberamos memoria
del aux
if modalidad==1:
    for i in range(k):
        E_1.append(E[i*npmax+modo])
        E_2.append(E[i*npmax+modo*2])
        E_3.append(E[i*npmax+modo*3])
        E_4.append(E[i*npmax+modo*4])
if modalidad==2:
    for i in range(k):
        E_1.append(E[i*npmax+1])
        E_2.append(E[i*npmax+2])
        E_3.append(E[i*npmax+modo])
        E_4.append(E[i*npmax+modo+1])

#--------------------------------
#datos
E1m=max(E_1)
E1n=max(E_1[int(k/10.):])
Eind=E_1.index(E1n)
if E1m<max(E_2):
    E1m=max(E_2)
    E1n=max(E_2[int(k/10.):])
    Eind=E_2.index(E1n)
tind=t[Eind]
Eperd=(E1m-E1n)*100./E1m
M1='Energía inicial: '+str(round(E1m,3))
M2='Energía 1º recurrencia: '+str(round(E1n,3))
M3='t recurrencia: '+str(round(tind,3))+' ciclos.'
M4='Energía perdida: '+str(round(Eperd,3))+' %'

aux1=0.#Energía inicial
aux2=0.#Energía final
for i in range(npmax):
    aux1+=E[i]
    aux2+=E[Eind*npmax+i]
    
M5='Energía no cons.: '+ str(round((aux2-aux1)*100./aux1, 4))+' %'
del E
#Auxiliares para el video
ai=max(u)
ae=min(u)
#--------------------------------
#Gráficas
#plt.close('all')#Cerramos las anteriores

if q==1:
    #Preparamos la gráfica
    plt.figure('Gráfica energías alpha={0} y amplitud={1}'.format(alfa, a), dpi=200.)
    #plt.title(r'N={0}, $\alpha$={1} y amplitud={2}'.format(npmax-2,alfa, a), fontsize=8)
    if modalidad==1:
        plt.plot(t, E_1, '.-', color='red', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo))
        plt.plot(t, E_2, '.-', color='blue', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo*2))
        plt.plot(t, E_3, '.-', color='green', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo*3))
        plt.plot(t, E_4, '.-', color='yellow', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo*4))
    elif modalidad==2:
        plt.plot(t, E_1, '.-', color='red', markersize=1., linewidth=0.3, label='Modo {0}'.format(1))
        plt.plot(t, E_2, '.-', color='blue', markersize=1., linewidth=0.3, label='Modo {0}'.format(2))
        plt.plot(t, E_3, '.-', color='green', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo))
        plt.plot(t, E_4, '.-', color='yellow', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo+1))
        
    plt.plot(t, [E1m]*k, ':', color='grey', linewidth=0.5)
    plt.plot(t, [E1n]*k, ':', color='grey', linewidth=0.5)
    
    '''
    texto1 = plt.text(-12, E1m*1.11, M1, fontsize=8)
    texto2 = plt.text(-12, E1m*1.08, M2, fontsize=8)
    texto3 = plt.text(t[-1]*2.45/7., E1m*1.11, M3, fontsize=8)
    texto4 = plt.text(t[-1]*7./10, E1m*1.11, M4, fontsize=8)
    texto5 = plt.text(t[-1]*7./10, E1m*1.08, M5, fontsize=8)
    '''
    plt.show()
    
    plt.xlabel(r'$\omega_1 t/2\pi$',fontsize=20);plt.ylabel('Energía',fontsize=20)
    plt.legend(loc='upper right', fontsize=15)

elif q==2:
    #Preparamos la gráfica
    plt.figure(figsize=(15, 6))
    plt.subplot(121)
    plt.tight_layout()
    plt.subplot(122)
    #plt.title(r'Energía de los modos con $\alpha$={0} y amplitud={1}'.format(alfa, a))
    plt.plot(t[int(k/2.)], 0.0, '.', color='white', markersize=1.)
    plt.xlabel('t (ciclos)', fontsize=15);plt.ylabel('Energía', fontsize=15)
    if modalidad==1:
        plt.plot(t[0], E_1[0], '.', color='red', label='Modo principal {0}'.format(modo))
        plt.plot(t[0], E_2[0], '.', color='blue', label='Modo {0}'.format(modo+1))
        plt.plot(t[0], E_3[0], '.', color='green', label='Modo {0}'.format(modo+2))
    if modalidad==2:
        plt.plot(t[0], E_1[0], '.', color='red', label='Modo principal {0}'.format(modo))
        plt.plot(t[0], E_2[0], '.', color='blue', label='Modo {0}'.format(modo+1))
        plt.plot(t[0], E_3[0], '.', color='green', label='Modo {0}'.format(modo*2))
    plt.tight_layout()
    plt.legend(loc='lower right', fontsize=15)
    plt.pause(2)
    for i in range(int(k/2.)):

        if i%4==0:
            plt.subplot(122)
            plt.plot(t[i], E_1[i], '.', color='red')
            plt.plot(t[i], E_2[i], '.', color='blue')
            plt.plot(t[i], E_3[i], '.', color='green')

            plt.subplot(121)
            plt.cla()
            plt.xlabel('x');plt.ylabel('u')
            plt.plot(0., ai, '.', color='white')
            plt.plot(0., ae, '.', color='white')
            plt.plot(x, u[i*npmax:i*npmax+npmax], '-', color='black', linewidth=3)
            plt.savefig('C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Figuras para gif\\N'+str(npmax-2)+'_alfa1\\N'+str(npmax-2)+'_'+str(i)+'.png', dpi=50)
            #plt.pause(0.01)
        
        if (i*1000)%k==0:
            print((i*100)/k)
    plt.subplot(122)    
    plt.plot(t, [E1m]*k, '-', color='grey', linewidth=0.5)
    plt.plot(t, [E1n]*k, '-', color='grey', linewidth=0.5)
    plt.show()