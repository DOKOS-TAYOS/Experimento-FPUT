#Datos de autor.
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Alejandro Mata Ali (DOKOS TAYOS)"
__copyright__ = "Public content for science use"
__version__ = "1.0.0"
__email__ = "alejandro.mata.ali@gmail.com"
#----------------------------------
import numpy as np
#--------------------------------
'''
Tipo de ordenación:
    tipo=1 Energías
    tipo=2 Solitones
    tipo=3 Espacios de Fase'''
tipo=3
tipo2='alfa'
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
#Energías
if tipo==1:
    if tipo2=='alfa':
        name='C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Programas\\Datos\\FPUT\\N'+str(npmax)+'\\datos_alpha'
    elif tipo2=='beta':
        name='C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Programas\\Datos\\FPUTbeta\\N'+str(npmax)+'\\datos_beta'
#Solitones
elif tipo==2:
    if tipo2=='alfa':
        name='C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Programas\\Datos\\Solitones_alpha\\N'+str(npmax)+'\\datos_alpha'
    elif tipo2=='dispersion':
        name='C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Programas\\Datos\\Dispersion\\N'+str(npmax)+'\\datos_alpha'
    elif tipo2=='beta':
        name='C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Programas\\Datos\\Solitones_beta\\N'+str(npmax)+'\\datos_beta'
#Espacios de fases
elif tipo==3:
    if tipo2=='alfa':
        name='C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Programas\\Datos\\Espacios de Fase\\N'+str(npmax)+'\\datos_alpha'
    elif tipo2=='beta':
        name='C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Programas\\Datos\\Espacios de Fase\\N'+str(npmax)+'\\datos_beta'
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

if tipo==1:
    t=[]
    u=[]
    E=[]
    
    cambio=npmax*2+1
    k=int((len(aux)-1)/cambio)
    
    omega12pi=2.*np.sin(np.pi/(2.*(npmax-1)))/(2.*np.pi)
    
    for i in range(k):
        t.append(float(aux[i*cambio])*omega12pi)
        for j in range(npmax):
            u.append(float(aux[i*cambio+1+j]))
            E.append(float(aux[i*cambio+1+npmax+j]))
            
    #Liberamos memoria
    del aux
    #Volvemos a guardar
    f = open(name, "w")
    for i in range(k):
        f.write(str(t[i])+"\n")
    for i in range(k):
        for j in range(npmax):
            f.write(str(u[i*npmax+j])+"\n")
    for i in range(k-1):
        for j in range(npmax):
            f.write(str(E[i*npmax+j])+"\n")
    for j in range(npmax-1):
        f.write(str(E[(k-1)*npmax+j])+"\n")
    f.write(str(E[(k-1)*npmax+npmax-1]))
    f.close()
elif tipo==2:
    t=[]
    u=[]
    E=[]
    
    cambio=npmax+2
    k=int((len(aux)-1)/cambio)
    
    omega12pi=2.*np.sin(np.pi/(2.*(npmax-1)))/(2.*np.pi)
    
    for i in range(k):
        t.append(float(aux[i*cambio])*omega12pi)
        for j in range(npmax):
            u.append(float(aux[i*cambio+1+j]))
        E.append(float(aux[i*cambio+1+npmax]))
            
    #Liberamos memoria
    del aux
        
    #--------------------------------
    #datos
    E1n=max(E[int(k/10.):])
    Eind=E.index(E1n)
    tind=t[Eind]
    tind=t.index(tind)
    
    del E
    del Eind
    
    #Volvemos a guardar
    f = open(name, "w")
    for i in range(k):
        f.write(str(t[i])+"\n")
    for i in range(k):
        for j in range(npmax):
            f.write(str(u[i*npmax+j])+"\n")
    f.write(str(tind))
    f.close()
elif tipo==3:
    u=[]
    v=[]
    
    cambio=npmax*2
    k=int((len(aux)-2)/cambio)
    
    omega12pi=2.*np.sin(np.pi/(2.*(npmax-1)))/(2.*np.pi)
    
    for i in range(k):
        for j in range(1,npmax-1):
            u.append(float(aux[i*cambio+j]))
            v.append(float(aux[i*cambio+npmax+j]))
    u1=[]
    v1=[]
    for part in range(npmax-2):
        for i in range(k):
            u1.append(u[i*(npmax-2)+part])
            v1.append(v[i*(npmax-2)+part])
    #Liberamos memoria
    del aux
    #Volvemos a guardar
    f = open(name, "w")
    for i in range(k*(npmax-2)):
        f.write(str(u1[i])+"\n")
    for i in range(k*(npmax-2)-1):
        f.write(str(v1[i])+"\n")
    f.write(str(v1[k*(npmax-2)-1]))
    f.close()
    
print('Datos Ordenados.')