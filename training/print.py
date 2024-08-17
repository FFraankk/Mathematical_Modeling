# -*- coding: utf-8 -*-

import os
import math
import numpy as np
import matplotlib.pyplot as plt




save_path =r'D:\Mathematical_Modeling\training\pics'
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False 

# 创建文件夹

if not os.path.exists(save_path):
    os.makedirs(save_path)

# 有读秒
def a1t0withCT(V0):
    a1=-0.045*(3.6*V0)**1.087
    t0=-1.926*math.log(3.6*V0)+8.703
    return a1,t0

# 无读秒
def a1t0withoutCT(V0):
    a1=-math.exp(2.340-52.329/(3.6*V0))
    t0=2.5*math.exp(-0.018*3.6*V0)  
    return a1,t0

CT=[0,1]
L=4
H=30*3.14*7/24
NT2=0
NT31=0
NT32=0
S_arry=np.linspace(21,40,20)
V0_arry=np.linspace(15,22,8)

def T_time(V0,VF,a1,t0,S,L,H):
    # T1=(V0-(V0**2+2*a1*(S+L+H-V0*t0))**0.5)/(-a1)+t0
    T2=(VF-V0)/a1 + (H+L-((VF**2-V0**2)/(2*a1))+S-V0*t0)/VF + t0
    T31=(VF-V0)/a1+(H+L+S-V0*t0-(VF**2-V0**2)/2*a1)/VF+t0
    T32=(2*(S-V0*t0))/(VF+V0)+(H+L)/VF+t0
    T_out=max(T31,T2,T32)

    # if T1==T_out:
    #     char='T1'
    if T2==T_out:
        char='T2'
    elif T31==T_out:
        char='T31'   
    else :
        char='T32'
    # print(V0**2+2*a1*(S+L+H-V0*t0))
    return char,T_out




for CT in CT:
    n=0
    for V0 in V0_arry:
        T_arry = []
        n=n+1
        for S in S_arry:
            if CT:
                a1,t0=a1t0withCT(V0)
            else:
                a1,t0=a1t0withoutCT(V0)
            
            
            char,T=T_time(V0,8.33,a1,t0,S,L,H)

            # print(char,'=',T)
            if char=='T2':
                NT2+=1
            if char=='T31':
                NT31+=1
            if char=='T32':
                NT32+=1
            T_arry.append(T)
            


        # plt.figure(figsize=(10, 6))
        

        if CT==1:
            print('1')
            plt.xlabel('S(m)')
            plt.ylabel('T (s)')
            plt.plot(S_arry, T_arry, label=f'V = {V0}')
            if n==4:
                
                plt.title(f'不同S下的时间曲线 (V0 = {V0}),有读秒')
                plt.legend()
                plt.grid(True)
                # plt.show()
                plt.savefig(f'{save_path}/Time_Curve_V0_WCT_{V0}.jpg')
                plt.close() 
                n=0
        if CT==0:
            print('1')
            plt.xlabel('S(m)')
            plt.ylabel('T (s)')
            plt.plot(S_arry, T_arry, label=f'S = {S}')
            if n==4:
                
                plt.title(f'不同S下的时间曲线 (V0 = {V0}),无读秒')
                plt.legend()
                plt.grid(True)
                # plt.show()
                plt.savefig(f'{save_path}/Time_Curve_V0_WOCT_{V0}.jpg')
                plt.close() 
                n=0
    
save_path

print(NT2,NT31,NT32)
        # print(S,V0)
