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
import math as math


nsolitones=2#Numero solitones
modo=-1#Modos de visualización
d3=1#0: 2d, 1: 3D
'''0: ver solitones
n: cantidad conservada n'''

A=[2.]#Amplitud solitones
x0=[-10.]#Posicion inicial solitones

long=10.#Longitud total visible (alrededor de x0[0])
dx=0.1#Espaciado de malla

tiempo=100#Intervalos de tiempo
dt=0.01#Tiempo por interacion

intervalo=1#Cada cuanto graficar
#-----------------------------------------------------------
params = {'xtick.labelsize': 25, 'ytick.labelsize': 25, 'font.size': 35}#
mpl.rcParams.update(params)
plt.close('all')
nodos=int(long/dx)
x=np.linspace(-long/2.,long/2.,nodos)

def soliton1(A, x, t):
    u=np.zeros(nodos)
    aux1=np.sqrt(A/2.)
    x=list(x-2.*A*t)
    for i in range(nodos):
        u[i]=1./(math.cosh(aux1*(x[i]-x0))**2)
    u=list(A*np.array(u))
    return u

def soliton2(A, x, t):
    u=np.zeros(nodos)
    x=list(x)
    for i in range(nodos):
        u[i]=(3+4*math.cosh(2*x[i]-8*t)+math.cosh(4*x[i]-64*t))/(3*math.cosh(x[i]-28*t)+math.cosh(3*x[i]-36*t))**2
    u=list(12.*np.array(u))
    return u


def derivada(u):
    u_der=[]
    for i in range(len(u)-1):
        u_der.append((u[i+1]-u[i])/dx)
    return u_der

def T1(u):
    t1=sum(u)*dx
    return t1

def T2(u):
    t1=0
    for i in range(len(u)):
        t1+=u[i]**2
    t1*=0.5*dx
    return t1

def T3(u):
    t1=0
    u_der=derivada(u)
    for i in range(len(u)-1):
        t1+=u[i]**3+0.5*u_der[i]**2
    t1*=dx
    return t1

if modo==0:
    if nsolitones==1:
        plt.figure('Solitones')
        for i in range(tiempo):
            t=dt*i
            u=soliton1(A[0],x,t)
            if i%intervalo==0:
                plt.cla()
                plt.plot(x, u, '-', color='black')
                plt.show()
                plt.pause(0.01)
            x=x+A[0]*dt
    elif nsolitones==2:
        plt.figure('Solitones')
        for i in range(tiempo):
            t=dt*(i-100)
            u=soliton2(A[0],x,t)
            if i%intervalo==0:
                plt.cla()
                plt.plot(x[0],8., color='white')
                plt.plot(x, u, '-', color='black')
                plt.show()
                plt.pause(0.01)
            x=x+2*3*dt

elif modo==1:
    plt.figure('Cantidad conservada 1')
    plt.title('Cantidad conservada 1')
    plt.xlabel('t');plt.ylabel('Masa')
    if nsolitones==1:
        for i in range(tiempo):
            t=dt*i
            u=soliton1(A[0],x,t)
            t1=T1(u)
            plt.plot(t, t1, '.', color='black')
            plt.show()
            x=x+2*A[0]*dt
    elif nsolitones==2:
        for i in range(tiempo):
            t=dt*i
            u=soliton2(A[0],x,t)
            t1=T1(u)
            plt.plot(t, t1, '.', color='black')
            plt.show()
            x=x+2*A[0]*dt



elif modo==2:
    plt.figure('Cantidad conservada 2')
    plt.title('Cantidad conservada 2')
    plt.xlabel('t');plt.ylabel('Momento')
    if nsolitones==1:
        for i in range(tiempo):
            t=dt*i
            u=soliton1(A[0],x,t)
            t1=T2(u)
            plt.plot(t, t1, '.', color='black')
            plt.show()
            x=x+2*A[0]*dt
    elif nsolitones==2:
        for i in range(tiempo):
            t=dt*i
            u=soliton2(A[0],x,t)
            t1=T2(u)
            plt.plot(t, t1, '.', color='black')
            plt.show()
            x=x+2*A[0]*dt




elif modo==3:
    plt.figure('Cantidad conservada 3')
    plt.title('Cantidad conservada 3')
    plt.xlabel('t');plt.ylabel('Energía')
    if nsolitones==1:
        for i in range(tiempo):
            t=dt*i
            u=soliton1(A[0],x,t)
            t1=T3(u)
            plt.plot(t, t1, '.', color='black')
            plt.show()
            x=x+2*A[0]*dt
    elif nsolitones==2:
        for i in range(tiempo):
            t=dt*i
            u=soliton2(A[0],x,t)
            t1=T3(u)
            plt.plot(t, t1, '.', color='black')
            plt.show()
            x=x+2*A[0]*dt




elif modo==-1:
    uabs=[]
    t=[]
    if nsolitones==1:
        for i in range(tiempo):
            t.append(dt*i)
            uabs.append(soliton1(A[0],x,t[i]))
    elif nsolitones==2:
        for i in range(tiempo):
           t.append(dt*i-tiempo*dt/2)
           uabs.append(soliton2(A[0],x,t[i]))
    
    xp=np.array([x]*tiempo)
    tf=np.array([t]*len(x))
    tf=np.transpose(tf)
    uabs=np.array(uabs)
    if d3==1:
                
        params = {'xtick.labelsize': 15, 'ytick.labelsize': 15, 'font.size': 20}#
        mpl.rcParams.update(params)
        #Para versión 3D
        plt.figure('Soliton 3D', dpi=200.)
        ax=plt.gca(projection='3d')
        #ax.set_title('Solitón 3D')
        ax.set_xlabel('t')
        ax.set_ylabel('x')
        ax.set_zlabel('u')
    
        surface=ax.plot_surface(tf,xp,uabs, cmap=cm.seismic)
        plt.show()
        
    elif d3==0:
        params = {'xtick.labelsize': 25, 'ytick.labelsize': 25, 'font.size': 35}#
        mpl.rcParams.update(params)
        plt.figure('Solitones KdV', dpi=150., figsize=[6,8])
        plt.ylabel('t')
        plt.xlabel('x')
        color=cm.CMRmap
        shade='gouraud'#auto, gouraud, nearest
        
        '''Colores:
            twilight    seismic    accent    accent_r    BuPu    CMRmap    GnBu    Greys    PuBu    PuOr
            Purples    RdBu    afmhot    binary    bwr    cooper    cubehelix    gist_stern    ocean
            '''
        
        #ax = fig.add_axes((0.121, 0.148, 0.995-0.121, 0.995-0.148))
        
        forma=0
        if forma==0:
            plt.pcolormesh(xp,tf,uabs, cmap=color, shading=shade)
        elif forma==1:
            plt.contourf(xp, tf, uabs,10, alpha=.75, cmap=color)
            C = plt.contour(xp, tf, uabs,10, colors='black', linewidths=0.5)
        plt.tight_layout()
        
        plt.show()
    
    del tf
    del xp