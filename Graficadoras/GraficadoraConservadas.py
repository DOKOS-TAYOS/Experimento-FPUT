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

'''

q=1

#Modo inicial
modo=1

#Modalidad
modalidad=1
#---------------------------------
#Parametros
alfa=0.25
a=1
npmax=32
aum=1#84*2/10.
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
u=[]

cambio=npmax*2+1
k=int((len(aux))/cambio)
aum=int(aum)

omega12pi=2.*np.sin(np.pi/(2.*(npmax-1)))/(2.*np.pi)
c=(npmax-1)*omega12pi*2.#Velocidad de la onda
print(c)
for i in range(k):
    t.append(float(aux[i])/omega12pi)


dt=t[1]-t[0]#Diferencia de tiempos
print(dt)
uaux=[]
for i in range(k,k*npmax+k):#Coge todos
    uaux.append(float(aux[i]))
    if (i-k+1)%npmax==0. and i!=k:#Divide los elementos por tiempo u[tiempo][espacio]
        u.append(uaux)
        uaux=[]

#nt=len(u)
#nx=len(u[0])
#Liberamos memoria
del aux, uaux

def d_r(ui):
    nt=len(ui)
    nx=len(ui[0])
    ux=[]
    ut=[]

    #Sin promedio
    for ti in range(nt-1):
        uaux=[]
        for xi in range(nx-1):
            uaux.append((ui[ti+1][xi]-ui[ti][xi])/(c*dt))
        ut.append(uaux)
    ut=np.array(ut)

    for ti in range(nt-1):
        uaux=[]
        for xi in range(nx-1):
            uaux.append(ui[ti][xi+1]-ui[ti][xi])
        ux.append(uaux)      
    ux=np.array(ux)
    
    return ux-ut

def d_rp(ui):
    nt=len(ui)
    nx=len(ui[0])
    ux=[]
    ut=[]
    uxr=[]
    utr=[]
    
    #Derivada y promedio.
    for ti in range(nt-1):
        uaux=[]
        for xi in range(nx):
            uaux.append((ui[ti+1][xi]-ui[ti][xi])/(c*dt))
        ut.append(uaux)
    ut=np.array(ut)
    
    for ti in range(nt-1):
        uaux=[]
        for xi in range(nx-1):
            uaux.append((ut[ti][xi+1]+ut[ti][xi])/2.)#promedio espacial
        utr.append(uaux)
    utr=np.array(utr)
    
    
    for ti in range(nt):
        uaux=[]
        for xi in range(nx-1):
            uaux.append(ui[ti][xi+1]-ui[ti][xi])
        ux.append(uaux)      
    ux=np.array(ux)
    
    for ti in range(nt-1):
        uaux=[]
        for xi in range(nx-1):
            uaux.append((ux[ti+1][xi]+ux[ti][xi])/2.)#promedio temporal
        uxr.append(uaux)
    uxr=np.array(uxr)

    return uxr-utr

def d_pr(ui):
    nt=len(ui)
    nx=len(ui[0])
    ux=[]
    ut=[]
    uxr=[]
    utr=[]

    #Promedio y derivada
    for ti in range(nt):
        uaux=[]
        for xi in range(nx-1):
            uaux.append((ui[ti][xi+1]+ui[ti][xi])/2.)#promedio espacial
        utr.append(uaux)
    utr=np.array(utr)
    
    
    for ti in range(nt-1):
        uaux=[]
        for xi in range(nx-1):
            uaux.append((utr[ti+1][xi]-utr[ti][xi])/(c*dt))
        ut.append(uaux)
    ut=np.array(ut)
    
    for ti in range(nt-1):
        uaux=[]
        for xi in range(nx):
            uaux.append((ui[ti+1][xi]+ui[ti][xi])/2.)#promedio temporal
        uxr.append(uaux)
    uxr=np.array(uxr)
    
    for ti in range(nt-1):
        uaux=[]
        for xi in range(nx-1):
            uaux.append(uxr[ti][xi+1]-uxr[ti][xi])
        ux.append(uaux)      
    ux=np.array(ux)

    return ux-ut
'''
def d_r_(ui):
    nt=len(ui)
    nx=len(ui[0])
    ux=[]
    ut=[]
    for ti in range(nt-1):
        uaux=[]
        for xi in range(1,nx):
            uaux.append((ui[ti+1][xi]-ui[ti][xi])/(c*dt))
        ut.append(uaux)
    ut=np.array(ut)
    for ti in range(nt-1):
        uaux=[]
        for xi in range(1,nx):
            uaux.append(ui[ti][xi]-ui[ti][xi-1])
        ux.append(uaux)      
    ux=np.array(ux)
    return ux-ut
'''
u0=d_pr(u)

I1=[]
#u0=np.transpose(u0)
for i in range(2*npmax, int(len(u0)/aum)):
    cont=0
    for j in range(len(u0[0])):
        for k in range(0,aum):
            cont+=u0[i*(k+1)-int(j/c)][j]
    cont=cont/aum
    I1.append(cont)

I2=[]
for i in range(2*npmax,int(len(u0)/aum)):
    cont=0
    for j in range(len(u0[0])):
        for k in range(0,aum):
            cont+=u0[i*aum-int(j/c)][j]**2 /2
    cont=cont/aum
    I2.append(cont)

u1=d_r(u0)
I3=[]
for i in range(2*npmax,int(len(u1)/aum)):
    cont=0
    for j in range(len(u1[0])):
        for k in range(0,aum):
            cont+=u0[i*aum-int(j/c)][j]**3 /3 - u1[i*aum-int(j/c)][j]**2
    cont=cont/aum
    I3.append(cont)


plt.close('all')
plt.figure('Gráfica T alpha={0} y amplitud={1}'.format(alfa, a), dpi=200.)
plt.title(r'N={0}, $\alpha$={1} y amplitud={2}'.format(npmax-2,alfa, a), fontsize=8)
plt.plot(t[:len(I1)], I1, '.-', color='red', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo))
plt.show()


plt.figure('Gráfica T alpha={0} y amplitud={1}2'.format(alfa, a), dpi=200.)
plt.title(r'N={0}, $\alpha$={1} y amplitud={2}'.format(npmax-2,alfa, a), fontsize=8)
plt.plot(t[:len(I2)], I2, '.-', color='red', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo))
plt.show()

plt.figure('Gráfica T alpha={0} y amplitud={1}3'.format(alfa, a), dpi=200.)
plt.title(r'N={0}, $\alpha$={1} y amplitud={2}'.format(npmax-2,alfa, a), fontsize=8)
plt.plot(t[:len(I3)], I3, '.-', color='red', markersize=1., linewidth=0.3, label='Modo {0}'.format(modo))
plt.show()
