#Datos de autor.
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Alejandro Mata Ali (DOKOS TAYOS)"
__copyright__ = "Public content for science use"
__version__ = "1.0.0"
__email__ = "alejandro.mata.ali@gmail.com"
#----------------------------------
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
    
from scipy.optimize import curve_fit
from decimal import Decimal
plt.close('all')

name='Valores.txt'

t=[]#Recurrencia simulación
st=[]
m=[]#Recurrencia modelo
amp=[]
n=[]
alfa=[]
#-----------------------------------------------
def f(x,a,b):
    y=[]
    for i in range(len(x)):
        y.append(a*x[i]+b)
    return y

#Número de puntos de cada ajuste.
nums=4
alfas=6
amps=8


file=open(name, 'r')
bas=file.read()
file.close()

bas=bas.strip()
bas=bas.split('\n')

#-----------------------------------------------------------------
params = {'xtick.labelsize': 25, 'ytick.labelsize': 25, 'font.size': 30}#
mpl.rcParams.update(params)
#N variable
print('N_variable')
for i in range(nums):
    aux2=bas[i].split(' ')
    t.append((float(aux2[0])))
    st.append(float(aux2[1]))
    n.append(float(aux2[3]))
    m.append(float(aux2[-1]))

ajuste=curve_fit(f,n,t, absolute_sigma=True, sigma=st)
a=ajuste[0][0]
b=ajuste[0][1]
y_Ajus=f(n,a,b)
sa=np.sqrt(np.diag(ajuste[1]))[0]
sb=np.sqrt(np.diag(ajuste[1]))[1]

chi=0
for i in range(len(m)):
    chi+=((t[i]-y_Ajus[i])**2/y_Ajus[i])
print('chi_cuadrado=', chi)

sa='%.1E'% Decimal(sa)
ususa=sa[4:];ususa=int(ususa)
a=round(a,1-ususa)
print('a={var} {inc}'.format(var=a, inc=sa))
sb='%.1E'% Decimal(sb)
ususb=sb[4:];ususb=int(ususb)
b=round(b,1-ususb)
print('b={var} {inc}'.format(var=b, inc=sb))

fig=plt.figure('N_variable', dpi=150., figsize=[9,6])
#plt.title(r'$R$ frente a $B$', fontsize=6)
ax = fig.add_axes((0.121, 0.148, 0.995-0.121, 0.995-0.148))
plt.plot(n, y_Ajus, '-', color='blue', markersize=8., linewidth=0.8, label='Ajuste')
plt.plot(n, m, 'v', color='limegreen', markersize=8., linewidth=0.3, label='Modelo')
plt.plot(n,t, '.', color='crimson', markersize=8., linewidth=0.3, label='Simulación')
plt.errorbar(n, t, fmt='.',markersize=0.03,elinewidth=0.3, yerr=st)

plt.ylabel(r'$\ln(T_R)$');plt.xlabel(r'$\ln(N)$')
plt.legend(loc='upper left', fontsize=27)
#plt.tight_layout()
plt.show()
    
    
#-----------------------------------------------------------------
#alfa variable
print('alfa_variable')
t=[]#Recurrencia simulación
st=[]
m=[]#Recurrencia modelo
amp=[]
n=[]
alfa=[]
for i in range(nums,nums+alfas):
    aux2=bas[i].split(' ')
    t.append((float(aux2[0])))
    st.append(float(aux2[1]))
    alfa.append(float(aux2[2]))
    m.append(float(aux2[-1]))

ajuste=curve_fit(f,alfa,t, absolute_sigma=True, sigma=st)
a=ajuste[0][0]
b=ajuste[0][1]
y_Ajus=f(alfa,a,b)
sa=np.sqrt(np.diag(ajuste[1]))[0]
sb=np.sqrt(np.diag(ajuste[1]))[1]

chi=0
for i in range(len(m)):
    chi+=((t[i]-y_Ajus[i])**2/y_Ajus[i])
print('chi_cuadrado=', chi)

sa='%.1E'% Decimal(sa)
ususa=sa[4:];ususa=int(ususa)
a=round(a,1-ususa)
print('a={var} {inc}'.format(var=a, inc=sa))
sb='%.1E'% Decimal(sb)
ususb=sb[4:];ususb=int(ususb)
b=round(b,1-ususb)
print('b={var} {inc}'.format(var=b, inc=sb))

fig=plt.figure('alfa_variable', dpi=150., figsize=[9,6])
#plt.title(r'$R$ frente a $B$', fontsize=6)
ax = fig.add_axes((0.16, 0.148, 0.995-0.16, 0.995-0.148))
plt.plot(alfa, y_Ajus, '-', color='blue', markersize=8., linewidth=0.8, label='Ajuste')
plt.plot(alfa, m, 'v', color='limegreen', markersize=8., linewidth=0.3, label='Modelo')
plt.plot(alfa,t, '.', color='crimson', markersize=8., linewidth=0.3, label='Simulación')
plt.errorbar(alfa, t, fmt='.',markersize=0.03,elinewidth=0.3, yerr=st)

plt.ylabel(r'$\ln(T_R)$');plt.xlabel(r'$\ln(\alpha)$')
plt.legend(loc='upper right', fontsize=27)
#plt.tight_layout()
plt.show()


#-----------------------------------------------------------------
#amplitud variable
print('amplitud_variable')
t=[]#Recurrencia simulación
st=[]
m=[]#Recurrencia modelo
amp=[]
n=[]
alfa=[]
for i in range(nums+alfas,nums+alfas+amps):
    aux2=bas[i].split(' ')
    t.append((float(aux2[0])))
    st.append(float(aux2[1]))
    amp.append(float(aux2[4]))
    m.append(float(aux2[-1]))

    
ajuste=curve_fit(f,amp,t, absolute_sigma=True, sigma=st)
a=ajuste[0][0]
b=ajuste[0][1]
y_Ajus=f(amp,a,b)
sa=np.sqrt(np.diag(ajuste[1]))[0]
sb=np.sqrt(np.diag(ajuste[1]))[1]

chi=0
for i in range(len(m)):
    chi+=((t[i]-y_Ajus[i])**2/y_Ajus[i])
print('chi_cuadrado=', chi)

sa='%.1E'% Decimal(sa)
ususa=sa[4:];ususa=int(ususa)
a=round(a,1-ususa)
print('a={var} {inc}'.format(var=a, inc=sa))
sb='%.1E'% Decimal(sb)
ususb=sb[4:];ususb=int(ususb)
b=round(b,1-ususb)
print('b={var} {inc}'.format(var=b, inc=sb))

fig=plt.figure('amp_variable', dpi=150., figsize=[9,6])
#plt.title(r'$R$ frente a $B$', fontsize=6)

ax = fig.add_axes((0.16, 0.148, 0.995-0.16, 0.98-0.148))
plt.plot(amp, y_Ajus, '-', color='blue', markersize=8., linewidth=0.8, label='Ajuste')
plt.plot(amp, m, 'v', color='limegreen', markersize=8., linewidth=0.3, label='Modelo')
plt.plot(amp,t, '.', color='crimson', markersize=8., linewidth=0.3, label='Simulación')
plt.errorbar(amp, t, fmt='.',markersize=0.03,elinewidth=0.3, yerr=st)

plt.ylabel(r'$\ln(T_R)$');plt.xlabel(r'$\ln(amplitud)$')
plt.legend(loc='upper right', fontsize=27)
#plt.tight_layout()
plt.show()