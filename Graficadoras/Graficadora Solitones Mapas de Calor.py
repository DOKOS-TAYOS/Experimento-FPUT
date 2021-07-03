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
from matplotlib import cm
#--------------------------------
tipo='alfa'
'''
Gráficas
q=1 Por encima
q=2 Solitones en 3d desfasados
q=3 Vídeo solitones
q=4 Solitones en 3d 
'''
q=2

#Modo inicial
modo=1

#Modalidad
modalidad=1
#---------------------------------
#Parametros
alfa=0.5
a=1
npmax=32
#--------------------------------
#Visual
factor=8.#Lupa
mov=-10
#--------------------------------
#Diseño
color=cm.seismic
shade='gouraud'#auto, gouraud, nearest
'''Colores:
    twilight    seismic    accent    accent_r    BuPu    CMRmap    GnBu    Greys    PuBu    PuOr
    Purples    RdBu    afmhot    binary    bwr    cooper    cubehelix    gist_stern    ocean
    '''
forma=0
'''
0=simple
1=contorno
'''
#--------------------------------
#Forma de hacer el nombre del archivo
if tipo=='alfa':
    name='C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Programas\\Datos\\Solitones_alpha\\N'+str(npmax)+'\\datos_alpha'
elif tipo=='dispersion':
    name='C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Programas\\Datos\\Dispersion\\N'+str(npmax)+'\\datos_alpha'
elif tipo=='beta':
    name='C:\\Users\\aleja\\OneDrive - Universidade de Santiago de Compostela\\Documentos\\4 curso\\TFG\\Programas\\Datos\\Solitones_beta\\N'+str(npmax)+'\\datos_beta'
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
#E=[]

factor=factor*10.

cambio=npmax+1#Cambiar +1 por +2
k=int((len(aux))/cambio)#Si descomentas, el -1 
'''
omega12pi=2.*np.sin(np.pi/(2.*(npmax-1)))/(2.*np.pi)

for i in range(k):
    t.append(float(aux[i*cambio])*omega12pi)
    for j in range(npmax):
        u.append(float(aux[i*cambio+1+j]))
    E.append(float(aux[i*cambio+1+npmax]))
        '''
for i in range(k):
    t.append(float(aux[i]))
    
for i in range(k,k*npmax+k):
    u.append(float(aux[i]))
tind=int(aux[k*npmax+k])
#Liberamos memoria
del aux

#--------------------------------
#datos
'''E1n=max(E[int(k/10.):])
Eind=E.index(E1n)
tind=t[Eind]
tind=t.index(tind)
del E
del Eind
print ('Datos recopilados.')'''
#--------------------------------
#Gráficas
plt.close('all')#Cerramos las anteriores
params = {'xtick.labelsize': 25, 'ytick.labelsize': 25, 'font.size': 35}#
mpl.rcParams.update(params)

if q==1:
    #campo diferencias
    nop=npmax-1
    xp=list(x[:-1])
    tn=int(k/factor)
    xp=np.array([xp]*tn)
    t1=np.array([t[:tn]]*nop)
    t2=np.array([t[tn:2*tn]]*nop)
    tf=np.array([t[int(tind-tn/2.):int(tind-tn/2.)+tn]]*nop)
    xp=np.transpose(xp)

    dif=[]
    for j in range(nop):
        aux=[]
        for i in range(0, tn):
            aux.append(u[i*npmax+j+1]-u[i*npmax+j])
        dif.append(aux)
    dif=np.array(dif)
    plt.figure('SolitonesFPUT', dpi=150.)
    #plt.title('Oscilación en el tiempo')
    plt.ylabel('t (ciclos)')
    plt.xlabel('x')

    plt.pcolormesh(xp,t1,dif, cmap=color, shading=shade)
    plt.show()
    del t1
    plt.pause(0.5)
    print ('Primera lista')
    dif=[]
    for j in range(nop):
        aux=[]
        for i in range(tn, 2*tn):
            aux.append(u[i*npmax+j+1]-u[i*npmax+j])
        dif.append(aux)
    dif=np.array(dif)
    plt.figure('SolitonesFPUT 2', dpi=150.)
    #plt.title('Oscilación en el tiempo 2')
    plt.ylabel('t (ciclos)')
    plt.xlabel('x')

    plt.pcolormesh(xp,t2,dif, cmap=color, shading=shade)
    plt.show()
    del t2
    print ('Segunda lista')
    plt.pause(0.5)
    dif=[]
    for j in range(nop):
        aux=[]
        for i in range(int(tind-tn/2.),int(tind-tn/2.)+tn):
            aux.append(u[i*npmax+j+1]-u[i*npmax+j])
        dif.append(aux)
    dif=np.array(dif)
    plt.figure('SolitonesFPUT recurr', dpi=150.)
    #plt.title('Oscilación en el tiempo recurrencia')
    plt.ylabel('t (ciclos)')
    plt.xlabel('x')

    plt.pcolormesh(xp,tf,dif, cmap=color, shading=shade)
    plt.show()
    del tf
    del xp
    del dif
    
elif q==2:
    #campo diferencias
    nop=npmax-1
    xp=list(x[:-1])
    tn=int(k/factor)
    xp=np.array([xp]*tn)
    tf=np.array([t[int(tind/4.-tn/2.)-mov:int(tind/4.-tn/2.)-mov+tn]]*nop)
    xp=np.transpose(xp)
    
    dif=[]
    for i in range(nop):
        aux=[]
        for j in range(int(tind/4.-tn/2.)-mov,int(tind/4.-tn/2.)-mov+tn):
            aux.append(u[j*npmax+i+1]-u[j*npmax+i])
        dif.append(aux)
    dif=np.array(dif)
    '''
    print(np.shape(tf))
    print(np.shape(xp))
    print(np.shape(dif))
    '''
    plt.figure('SolitonesFPUT', dpi=150.)
    #plt.title(r'Movimiento solitonico N={0}, modo {1}, $\alpha=${2}'.format(npmax-2, modo, alfa))
    plt.ylabel('t (ciclos)')
    plt.xlabel('x')
    if forma==0:
        plt.pcolormesh(xp,tf,dif, cmap=color, shading=shade)
    elif forma==1:
        plt.contourf(xp, tf, dif,10, alpha=.75, cmap=color)
        C = plt.contour(xp, tf, dif,10, colors='black', linewidths=0.5)
#    plt.colorbar()
    plt.show()
    del tf
    del xp
    del dif

elif q==3:
    #Preparamos la gráfica
    am=a/4.
    nop=npmax-1
    xp=x[:-1]
    plt.figure(1)
    plt.pause(2)
    for i in range(k):
        if i%20==0:
            dif=[]
            for j in range(nop):
                dif.append(u[i*npmax+j+1]-u[i*npmax+j])
            plt.cla()
            
            plt.plot(0., am, '.', color='white')
            plt.plot(0., -am, '.', color='white')

            plt.plot(xp, dif, '-o', color='black', markersize=2.)
            plt.show()
            plt.pause(0.01)
            
elif q==4:
    #campo diferencias
    nop=npmax-1
    xp=list(x[:-1])
    tn=int(k/factor)
    xp=np.array([xp]*tn)
    tf=np.array([t[int(tind/2.-tn/2.)-mov:int(tind/2.+tn/2.)-mov]]*nop)
    xp=np.transpose(xp)
    
    dif=[]
    for j in range(nop):
        aux=[]
        for i in range(int(tind/2.-tn/2.)-mov,int(tind/2.+tn/2.)-mov):
            aux.append(u[i*npmax+j+1]-u[i*npmax+j])
        dif.append(aux)
    dif=np.array(dif)
    '''
    print(np.shape(tf))
    print(np.shape(xp))
    print(np.shape(dif))
    '''
    plt.figure('SolitonesFPUT recurr', dpi=150.)
    #plt.title(r'Movimiento solitonico N={0}, modo {1}, $\alpha=${2}'.format(npmax-2, modo, alfa))
    plt.ylabel('t (ciclos)')
    plt.xlabel('x')

    plt.pcolormesh(xp,tf,dif, cmap=color, shading=shade)
    plt.show()
    del tf
    del xp
    del dif
