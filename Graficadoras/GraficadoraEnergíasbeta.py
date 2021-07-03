#Datos de autor.
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Alejandro Mata Ali (DOKOS TAYOS)"
__copyright__ = "Public content for science use"
__version__ = "1.0.0"
__email__ = "alejandro.mata.ali@gmail.com"
#----------------------------------
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from Notas import *

#--------------------------------
'''
Gráfica
q=1 Gráfica energías
q=2 Gráfica en tiempo real
q=3 Sonido
'''

q=1

#Modo inicial
modo=2

#Modalidad
modalidad=1
#---------------------------------
#Parametros
beta=10
a=1
npmax=32
#--------------------------------
#Para música
notas=[do,mi,sol,si]
volbase=0.1
velocidad=4.
#-------------------------------
#Forma de hacer el nombre del archivo
name='C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Programas\\Datos\\FPUTbeta\\N'+str(npmax)+'\\datos_beta'

if beta<1.and beta!=0:
    aux='{:.2f}'.format(beta)
    name=name+'_'+aux[2:]
elif beta==0:
    name=name+'_0'
else:
    name=name+str(beta)
    
if a<1.:
    aux='{:.2f}'.format(a)
    name=name+'_a_'+aux[2:]
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
        E_2.append(E[i*npmax+modo*3])
        E_3.append(E[i*npmax+modo*5])
        E_4.append(E[i*npmax+modo*7])
if modalidad==2:
    for i in range(k):
        E_1.append(E[i*npmax+modo])
        E_2.append(E[i*npmax+modo+1])
        E_3.append(E[i*npmax+modo*2])
        E_4.append(E[i*npmax+(modo+1)*2])
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
M1='Energia inicial: '+str(round(E1m,3))
M2='Energia primera recurrencia: '+str(round(E1n,3))
M3='Tiempo recurrencia: '+str(round(tind,3))+' ciclos.'
M4='Porcentaje de energía perdida: '+str(round(Eperd,3))+' %'

aux1=0.#Energía inicial
aux2=0.#Energía final
for i in range(npmax):
    aux1+=E[i]
    aux2+=E[Eind*npmax+i]
    
M5='Proporción de energía no conservada: '+ str(round((aux2-aux1)*100./aux1, 4))+' %'
del E
#Auxiliares para el video
ai=max(u)
ae=min(u)
#--------------------------------
#Gráficas
plt.close('all')#Cerramos las anteriores
params = {'xtick.labelsize': 30, 'ytick.labelsize': 30, 'font.size': 30}#
mpl.rcParams.update(params)


if q==1:
    #Preparamos la gráfica
    fig=plt.figure('Gráfica de energías beta={0} y amplitud={1}'.format(beta, a), dpi=150., figsize=[12,6])
    #plt.title(r'Energía de los modos con $\beta$={0} y amplitud={1}'.format(beta, a), fontsize=6)
    ax = fig.add_axes((0.08, 0.155, 0.997-0.08, 0.997-0.155))
    #ax = fig.add_axes((0.08, 0.155, 0.997-0.08, 0.997-0.155))
    if modalidad==1:
        plt.plot(t, E_1, '.-', color='red', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo))
        plt.plot(t, E_2, '.-', color='blue', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo*3))
        plt.plot(t, E_3, '.-', color='green', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo*5))
        plt.plot(t, E_4, '.-', color='gold', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo*7))
    elif modalidad==2:
        plt.plot(t, E_1, '.-', color='red', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo))
        plt.plot(t, E_2, '.-', color='blue', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo+1))
        plt.plot(t, E_3, '.-', color='green', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo*2))
        plt.plot(t, E_4, '.-', color='gold', markersize=1., linewidth=0.3, label='Modo {0}'.format((modo+1)*2))
    
    plt.plot(t, [E1m]*k, '-', color='grey', linewidth=0.5)
    plt.plot(t, [E1n]*k, '-', color='grey', linewidth=0.5)
    
    plt.plot(t, [E1m]*k, ':', color='grey', linewidth=0.5)
    plt.plot(t, [E1n]*k, ':', color='grey', linewidth=0.5)
    '''
    from matplotlib.ticker import MaxNLocator
    ax.yaxis.set_major_locator(MaxNLocator(3)) '''
    plt.yticks(rotation='vertical')
    
    '''
    texto1 = plt.text(-12, E1m*1.11, M1, fontsize=8)
    texto2 = plt.text(-12, E1m*1.08, M2, fontsize=8)
    texto3 = plt.text(t[-1]*2.45/7., E1m*1.11, M3, fontsize=8)
    texto4 = plt.text(t[-1]*7./10, E1m*1.11, M4, fontsize=8)
    texto5 = plt.text(t[-1]*7./10, E1m*1.08, M5, fontsize=8)
    '''
    
    plt.xlabel(r'$\omega_1 t/2\pi$');plt.ylabel('Energía')
    
    leg = plt.legend(loc='lower right', fontsize=25)
    leg_lines = leg.get_lines()
    plt.setp(leg_lines, linewidth=4)

    plt.show()
elif q==2:
    #Preparamos la gráfica
    plt.subplot(121)
    plt.subplot(122)
    plt.title(r'Energía de los modos con $\beta$={0} y amplitud={1}'.format(beta, a))
    plt.plot(t[-1], 0.0, '.', color='white', markersize=1.)
    plt.xlabel('t (ciclos)');plt.ylabel('Energía')
    plt.plot(t[0], E_1[0], '.', color='red', label='Modo fundamental')
    plt.plot(t[0], E_2[0], '.', color='blue', label='Modo 2')
    plt.plot(t[0], E_3[0], '.', color='green', label='Modo 3')
#    plt.plot(t[0], E_4[0], '.', color='yellow', markersize=1., label='Modo 4')
    
    plt.legend(loc='upper right')
    plt.pause(2)
    for i in range(k):

        if i%10==0:
            plt.subplot(122)
            plt.plot(t[i], E_1[i], '.', color='red')
            plt.plot(t[i], E_2[i], '.', color='blue')
            plt.plot(t[i], E_3[i], '.', color='green')
#            plt.plot(t[i], E_4[i], '.', color='yellow', markersize=1.)

            plt.subplot(121)
            plt.cla()
            plt.plot(0., ai, '.', color='white')
            plt.plot(0., ae, '.', color='white')
            plt.plot(x, u[i*npmax:i*npmax+npmax], '-o', color='black', markersize=2.)
            plt.show()
            plt.pause(0.01)

    plt.subplot(122)    
    plt.plot(t, [E1m]*k, '-', color='grey', linewidth=0.5)
    plt.plot(t, [E1n]*k, '-', color='grey', linewidth=0.5)
    plt.show()
    
elif q==3:
    print('Empezamos a sonar')
    #Haremos música
    velocidad=1./(1000.*velocidad)
    #Normalizo
    E1=[]
    E2=[]
    E3=[]
    E4=[]
    for i in range(k):
        E1.append(E_1[i]/E1m)
        E2.append(E_2[i]/E1m)
        E3.append(E_3[i]/E1m)
        E4.append(E_4[i]/E1m)

    #---------------------------
    for i in range(1,len(notas)):
        if notas[i]<notas[i-1]:
            for j in range(i,len(notas)):
                notas[j]*=2.
    volumen=[E1[0],E2[0],E3[0],E4[0]]
    #---------------------------
    '''
    plt.title(r'Energía de los modos con $\alpha$={0} y amplitud={1}'.format(alfa, a))
    plt.plot(t[-1], 0.0, '.', color='white', markersize=1.)
    plt.xlabel('t (ciclos)');plt.ylabel('Energía')'''
    server = Server().boot()
    server.amp=volbase
    server.start()
    sine=[]
    #hr=[]
    for i in range(len(notas)):
        sine.append(Sine(notas[i], mul=volumen[i]).out())
        #hr.append(Harmonizer(sine[i]).out())
    final=Scope(sum(sine))
    for i in range(1,k):
        sine[0].mul=E1[i]
        sine[1].mul=E2[i]
        sine[2].mul=E3[i]
        sine[3].mul=E4[i]
        
        #hr[0].mul=E1[i]/2.
        #hr[1].mul=E2[i]/2.
        #hr[2].mul=E3[i]/2.
        #hr[3].mul=E4[i]/2.
        
        sleep(velocidad)
        '''
        plt.plot(t[i], E_1[i], '.', color='red')
        plt.plot(t[i], E_2[i], '.', color='blue')
        plt.plot(t[i], E_3[i], '.', color='green')
        plt.plot(t[i], E_4[i], '.', color='yellow')
        plt.show()'''

    server.stop()
    del E1,E2,E3,E4
print('Acabado.')