# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 18:12:28 2020

@author: Alejandro Mata Ali
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#--------------------------------
#Modo inicial
modo=1

#Modalidad
modalidad=1
#---------------------------------
#Parametros
alfa=0.25
a=1
npmax=16
#--------------------------------
#Forma de hacer el nombre del archivo
name='C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Programas\\Datos\\Superrec\\N'+str(npmax)+'\\datos_alpha'

if alfa<1.:
    aux='{:.2f}'.format(alfa)
    name=name+'_'+aux[2:]
else:
    name=name+str(alfa)
    
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
E=[]

E_1=[]
E_2=[]
E_3=[]
E_4=[]

cambio=npmax+1
k=int((len(aux)-1)/cambio)

omega12pi=2.*np.sin(np.pi/(2.*(npmax-1)))/(2.*np.pi)

for i in range(k):
    t.append(float(aux[i*cambio])*omega12pi)
    for j in range(npmax):
        E.append(float(aux[i*cambio+1+j]))
        
#Liberamos memoria
del aux
if modalidad==1:
    for i in range(k):
        E_1.append(E[i*npmax+modo])
        E_2.append(E[i*npmax+modo+1])
        E_3.append(E[i*npmax+modo+2])
        E_4.append(E[i*npmax+modo+3])
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
M2='Energia superrecurrencia: '+str(round(E1n,3))
M3='Tiempo superrecurrencia: '+str(round(tind,3))+' ciclos.'
M4='Porcentaje de energía perdida: '+str(round(Eperd,3))+' %'

aux1=0.#Energía inicial
aux2=0.#Energía final
for i in range(npmax):
    aux1+=E[i]
    aux2+=E[Eind*npmax+i]
    
M5='Proporción de energía no conservada: '+ str(round((aux2-aux1)*100./aux1, 4))+' %'
del E
#--------------------------------
#Gráficas
plt.close('all')#Cerramos las anteriores
params = {'xtick.labelsize': 30, 'ytick.labelsize': 30, 'font.size': 30}#
mpl.rcParams.update(params)

#Preparamos la gráfica
fig=plt.figure('Energías superrecurrencia', dpi=150., figsize=[12,6])

ax = fig.add_axes((0.08, 0.155, 0.997-0.08, 0.997-0.155))
#plt.title(r'Energía de los modos con N={0}, $\alpha$={1} y amplitud={2}'.format(npmax-2,alfa, a), fontsize=6)
if modalidad==1:
    plt.plot(t, E_1, '.-', color='red', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo))
    plt.plot(t, E_2, '.-', color='blue', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo*2))
    plt.plot(t, E_3, '.-', color='green', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo*3))
    plt.plot(t, E_4, '.-', color='gold', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo*4))
elif modalidad==2:
    plt.plot(t, E_1, '.-', color='red', markersize=1., linewidth=0.3, label='Modo {0}'.format(1))
    plt.plot(t, E_2, '.-', color='blue', markersize=1., linewidth=0.3, label='Modo {0}'.format(2))
    plt.plot(t, E_3, '.-', color='green', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo))
    plt.plot(t, E_4, '.-', color='gold', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo+1))
    
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
plt.legend(loc='lower right')

leg = plt.legend(loc='lower right', fontsize=25)
leg_lines = leg.get_lines()
plt.setp(leg_lines, linewidth=4)
    
plt.show()
