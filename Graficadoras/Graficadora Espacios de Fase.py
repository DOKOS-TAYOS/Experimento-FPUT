#Datos de autor.
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Alejandro Mata Ali (DOKOS TAYOS)"
__copyright__ = "Public content for science use"
__version__ = "1.0.0"
__email__ = "alejandro.mata.ali@gmail.com"
#----------------------------------
import numpy as np
import matplotlib.pyplot as plt
#--------------------------------
'''
Gráfica
q=1 Un modo
q=2 Todos los modos
'''

q=2

part=1

#Modo inicial
modo=1

#Modalidad
modalidad=1
#---------------------------------
#Parametros
alfa=0.25
a=1
npmax=3
#--------------------------------
#Forma de hacer el nombre del archivo
name='C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Programas\\Datos\\Espacios de Fase\\N'+str(npmax)+'\\datos_alpha'

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

del b

u=[]
v=[]
part-=1

cambio=npmax*2
k=int((len(aux))/cambio)#Cambia -2 por -1
for i in range(k*npmax):
    u.append(float(aux[i]))
for i in range(k*npmax, 2*k*npmax):
    v.append(float(aux[i]))
#Liberamos memoria
del aux

#--------------------------------
#Gráficas
plt.close('all')#Cerramos las anteriores

if q==1:
    u1=[]
    v1=[]
    for i in range(k*part,k*part+k):
        u1.append(u[i])
        v1.append(v[i])
    #Preparamos la gráfica
    plt.figure('Espacio de fase partícula {0}'.format(part+1), dpi=200.)
    plt.title(r'Espacio de fase partícula {0} con $\alpha$={1} y amplitud={2}'.format(part+1,alfa, a))
    plt.plot(u1, v1, '.-', color='crimson', markersize=0.2, linewidth=0.1)

    plt.show()
    
    plt.xlabel(r'$u$');plt.ylabel('Momento')

elif q==2:
    #Preparamos la gráfica
    plt.figure('Espacio de fase todas las partículas', dpi=200.)
    plt.title(r'Espacio de fase todas las partículas con $\alpha$={0} y amplitud={1}'.format(alfa, a))
    for j in range(npmax):
        aos=(j/npmax)
        aux=np.sin(2.*np.pi*j/npmax)**2
        u1=[]
        v1=[]
        col=(1-aux, aux*(1.-aux), aux*aux, 1.-aos)
        for i in range(k):
            ab=j*k
            u1.append(u[ab+i])
            v1.append(v[ab+i])
        plt.plot(u1, v1, '.-', color=col, markersize=0.3, linewidth=0.2, label='Partícula {0}'.format(j+1))

    plt.show()
    plt.legend(loc='upper right', fontsize=5)
    plt.xlabel(r'$u$');plt.ylabel('Momentos')
    '''
    #Preparamos la gráfica
    plt.figure('Espacio de fase todos los modos')
    plt.title(r'Espacio de fase todos los modos con $\alpha$={0} y amplitud={1}'.format(alfa, a))
    plt.plot(u, v, '.-', color='blue', markersize=1., linewidth=0.3)

    plt.show()
    
    plt.xlabel(r'$u$');plt.ylabel('Momentos')
    '''
