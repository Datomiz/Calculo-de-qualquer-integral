# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 17:03:41 2024

@author: Davi Tosta Miranda
"""

import numpy as np

#integral sem integral

equacao_chata = "-46.71446805737014 -4.190094994550975*x**1 + 0.010680635497267055*x**2 -2.705997363486788e-36*2**x + 41.26876422433497*x**(1/2)"

exatidao = 0.1

inicio = 0

fim = 124.32


vx = list(np.arange(inicio,fim+exatidao,exatidao))
vy = []

for x in vx:
    
    y = eval(equacao_chata)
    
    vy.append(y)
    
    
def integral_sem_integral(vx,vy):
    
    area = 0

    for i in range(len(vx)-1):
        
        h_tri = vy[i] - vy[i+1]
        # h_tri = abs(vy[i] - vy[i+1])
        
        base  =  vx[i+1] - vx[i]
        
        h_ret = min([(vy[i]),vy[i+1]])
        # h_ret = min([abs(vy[i]),abs(vy[i+1])])

        a_tri =  (base * h_tri)/2
        
        a_ret = base * h_ret
        
        # ou
        
        #a_trap = (min([vy[i],vy[i+1]]) +(min([vy[i],vy[i+1]])+abs(vy[i] - vy[i+1])))*(vx[i+1] - vx[i])/2

        area = area + a_tri + a_ret
    
    return(area)

resultado = integral_sem_integral(vx, vy)

#for i in range(len(vy)):

    #vy[i] = float(vy[i])
    #vx[i] = float(vx[i])

#print(f"{vx = }")
#print(f"{vy = }")

print(f"\nA integral de sua função é: {resultado}")
