import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

save_path =r'D:\Mathematical_Modeling\training\pics'
path1 =r'D:\Mathematical_Modeling\training\rate.csv'

if not os.path.exists(save_path):
    os.makedirs(save_path)

plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False 

CT=[0,1] # Countdown or not
L=4 # lenth of cars
Hwan=30*3.14*7/24 # Intersection width
Hzhi=30
NT2=0;NT31=0;NT32=0 # counters
S_arry=np.linspace(21,40,20) # Distance to the stop line
V0_arry=np.linspace(15,22,8) # Initial Velocity
T_counter=[] # us
t_counter=[] # normal




def a1t0withCT(V):
    a1=-0.045*(3.6*V)**1.087
    t0=-1.926*math.log(3.6*V)+8.703
    return a1,t0

# without Countdown
def a1t0withoutCT(V):
    a1=-math.exp(2.340-52.329/(3.6*V))
    t0=2.5*math.exp(-0.018*3.6*V)
    return a1,t0


def T_time(V0,VF,a1,t0,S,L,H):
    judge1=V0*t0-V0**2/(2*a1)
    
    judge2=V0*t0+(VF**2-V0**2)/(2*a1)
    # print(judge1,judge2)
    if (S>judge1):
        print('寄')
        return (float('nan'),float('nan'),float('nan'))
    if(S<=judge1):
        if (judge2>S+L+H):
            T1=(V0-(V0**2+2*a1*(S+L+H-V0*t0))**0.5)/(-a1)+t0
            t1_pass=(-V0+(V0**2-2*a1*(V0*t0-S-L))**0.5)/a1+t0
            # print(T1,V0,S,'1')
            return(T1,t1_pass)
        
        if(S<judge2<=S+L+H):
            T2=(VF-V0)/a1 + (H+L-((VF**2-V0**2)/(2*a1))+S-V0*t0)/VF + t0
            t2_pass=(-V0+(V0**2-2*a1*(V0*t0-S-L))**0.5)/a1+t0
            # print(T2,V0,S,'2')
            return(T2,t2_pass)
        
        if(S>judge2>0):
            T31=(VF-V0)/a1+(H+L+S-V0*t0-(VF**2-V0**2)/(2*a1))/VF+t0
            t31_pass=2*(S-V0*t0)/(VF+V0)+L/VF+t0
            # print(T31,V0,S,'3')
            return(T31,t31_pass)


def bianli(CT,S_arry,V0_arry):
    T_final=[]
    t_final=[]

    for CT1 in CT:
        n=0
        for S in S_arry:
            T_arry = []
            t_arry = []
            n=n+1
            for V0 in V0_arry:
                if CT1:
                    a1,t0=a1t0withCT(V0)
                else:
                    a1,t0=a1t0withoutCT(V0)
                T,t=T_time(V0,8.33,a1,t0,S,L,Hzhi)
                T_final.append(T)
                t_final.append(t)
                T_arry.append(T)
                t_arry.append(t)
                # print(T,t,S,V0)
            if CT1==1:
                # print('1')
                plt.xlabel('V0 (m/s)')
                plt.ylabel('T (s)')
                plt.plot(V0_arry, T_arry, label=f'S = {S}')
                if n==5:
                    plt.title(f'直行且有读秒情况下，不同S下的黄灯时间曲线 (S ={S-4}-{S})')
                    plt.legend()
                    plt.grid(True)
                    # plt.show()
                    plt.savefig(f'{save_path}/Time_Curve_S_WCT_STR{S:.2f}.jpg')
                    plt.close() 
                    n=0
            if CT1==0:
                # print('1')
                plt.xlabel('V0 (m/s)')
                plt.ylabel('T (s)')
                plt.plot(V0_arry, T_arry, label=f'S = {S}')
                if n==5:
                    plt.title(f'直行且无读秒情况下，不同S下的黄灯时间曲线 (S ={S-4}-{S})')            
                    plt.legend()
                    plt.grid(True)
                    # plt.show()
                    plt.savefig(f'{save_path}/Time_Curve_S_WOCT_STR{S:.2f}.jpg')
                    plt.close() 
                    n=0
        for V0 in V0_arry:
            T_arry = []
            n=n+1
            for S in S_arry:
                if CT1:
                    a1,t0=a1t0withCT(V0)
                else:
                    a1,t0=a1t0withoutCT(V0)
                
                T,t=T_time(V0,8.33,a1,t0,S,L,Hzhi)
                T_final.append(T)
                t_final.append(t)
                T_arry.append(T)
                t_arry.append(t)
                # print(T,t,S,V0)      
            if CT1==1:
                # print('1')
                plt.xlabel('S(m)')
                plt.ylabel('T (s)')
                plt.plot(S_arry, T_arry, label=f'V = {V0}')
                if n==4:
                    plt.title(f'直行且有读秒情况下，不同V0下的黄灯时间曲线 (V0 ={V0-3}-{V0})')
                    plt.legend()
                    plt.grid(True)
                    # plt.show()
                    plt.savefig(f'{save_path}/Time_Curve_V0_WCT_STR{V0}.jpg')
                    plt.close() 
                    n=0
            if CT1==0:
                # print('1')
                plt.xlabel('S(m)')
                plt.ylabel('T (s)')
                plt.plot(S_arry, T_arry, label=f'V = {V0}')
                if n==4:
                    plt.title(f'直行且无读秒情况下，不同V0下的黄灯时间曲线 (V0 ={V0-3}-{V0})')
                    plt.legend()
                    plt.grid(True)
                    # plt.show()
                    plt.savefig(f'{save_path}/Time_Curve_V0_WOCT_STR{V0}.jpg')
                    plt.close() 
                    n=0


    for CT1 in CT:
        n=0
        for S in S_arry:
            T_arry = []
            t_arry = []
            n=n+1
            for V0 in V0_arry:
                if CT1:
                    a1,t0=a1t0withCT(V0)
                else:
                    a1,t0=a1t0withoutCT(V0)
                T,t=T_time(V0,8.33,a1,t0,S,L,Hwan)
                T_final.append(T)
                t_final.append(t)
                T_arry.append(T)
                t_arry.append(t)
                # print(T,t,S,V0)
            if CT1==1:
                # print('1')
                plt.xlabel('V0 (m/s)')
                plt.ylabel('T (s)')
                plt.plot(V0_arry, T_arry, label=f'S = {S}')
                if n==5:
                    plt.title(f'转弯且有读秒情况下，不同S下的黄灯时间曲线 (S ={S-4}-{S})')
                    plt.legend()
                    plt.grid(True)
                    # plt.show()
                    plt.savefig(f'{save_path}/Time_Curve_S_WCT_STR{S:.2f}.jpg')
                    plt.close() 
                    n=0
            if CT1==0:
                # print('1')
                plt.xlabel('V0 (m/s)')
                plt.ylabel('T (s)')
                plt.plot(V0_arry, T_arry, label=f'S = {S}')
                if n==5:
                    plt.title(f'转弯且无读秒情况下，不同S下的黄灯时间曲线 (S ={S-4}-{S})')            
                    plt.legend()
                    plt.grid(True)
                    # plt.show()
                    plt.savefig(f'{save_path}/Time_Curve_S_WOCT_STR{S:.2f}.jpg')
                    plt.close() 
                    n=0
        for V0 in V0_arry:
            T_arry = []
            n=n+1
            for S in S_arry:
                if CT1:
                    a1,t0=a1t0withCT(V0)
                else:
                    a1,t0=a1t0withoutCT(V0)
                
                T,t=T_time(V0,8.33,a1,t0,S,L,Hwan)
                T_final.append(T)
                t_final.append(t)
                T_arry.append(T)
                t_arry.append(t)
                # print(T,t,S,V0)      
            if CT1==1:
                # print('1')
                plt.xlabel('S(m)')
                plt.ylabel('T (s)')
                plt.plot(S_arry, T_arry, label=f'V = {V0}')
                if n==4:
                    plt.title(f'转弯且有读秒情况下，不同V0下的黄灯时间曲线 (V0 ={V0-3}-{V0})')
                    plt.legend()
                    plt.grid(True)
                    # plt.show()
                    plt.savefig(f'{save_path}/Time_Curve_V0_WCT_STR{V0}.jpg')
                    plt.close() 
                    n=0
            if CT1==0:
                # print('1')
                plt.xlabel('S(m)')
                plt.ylabel('T (s)')
                plt.plot(S_arry, T_arry, label=f'S = {V0}')
                if n==4:
                    plt.title(f'转弯且无读秒情况下，不同V0下的黄灯时间曲线 (V0 ={V0-3}-{V0})')
                    plt.legend()
                    plt.grid(True)
                    # plt.show()
                    plt.savefig(f'{save_path}/Time_Curve_V0_WOCT_{V0}.jpg')
                    plt.close() 
                    n=0
    return T_final,t_final



T_pass,t_pass=bianli(CT,S_arry,V0_arry)
# print(len(T_pass))
# print(len(t_pass))

T_rate_arry=[]
t_rate_arry=[]
for t in [3,4,5,6,7,8]:
    T_count_greater_than_T = sum(1 for item in T_pass if item < t)     
    t_count_greater_than_t = sum(1 for item in t_pass if item < t)
    
    print(f'T={t}时，通过率是{T_count_greater_than_T/len(T_pass)}')
    print(f't={t}时，通过率是{t_count_greater_than_t/len(t_pass)}')

    T_rate_arry.append(100*(T_count_greater_than_T/len(T_pass))) 
    t_rate_arry.append(100*(t_count_greater_than_t/len(t_pass))) 

df = pd.DataFrame({'黄灯时长(s)': [3,4,5,6,7,8], '通过对侧停止线百分比(%)': T_rate_arry,'通过停止线车辆百分比(%)':t_rate_arry })

df.to_csv(path1,index=False)

