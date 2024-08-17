# # -*- coding: utf-8 -*-

# import os
# import math
# import numpy as np
# import matplotlib.pyplot as plt


# save_path =r'D:\Mathematical_Modeling\training\pics'

# if not os.path.exists(save_path):
#     os.makedirs(save_path)

# plt.rcParams['font.sans-serif'] = ['SimHei'] 
# plt.rcParams['axes.unicode_minus'] = False 

# CT=[0,1] # Countdown or not
# L=4 # lenth of cars
# Hwan=30*3.14*7/24 # Intersection width
# Hzhi=30
# NT2=0;NT31=0;NT32=0 # counters
# S_arry=np.linspace(21,40,20) # Distance to the stop line
# V0_arry=np.linspace(15,22,8) # Initial Velocity
# T_counter=[] # us
# t_counter=[] # normal


# # with Countdown
# def a1t0withCT(V0):
#     a1=-0.045*(3.6*V0)**1.087
#     t0=-1.926*math.log(3.6*V0)+8.703
#     return a1,t0

# # without Countdown
# def a1t0withoutCT(V0):
#     a1=-math.exp(2.340-52.329/(3.6*V0))
#     t0=2.5*math.exp(-0.018*3.6*V0)  
#     return a1,t0

# # functions in
# def T_time(V0,VF,a1,t0,S,L,H):
#     # T1=(V0-(V0**2+2*a1*(S+L+H-V0*t0))**0.5)/(-a1)+t0
#     T2=(VF-V0)/a1 + (H+L-((VF**2-V0**2)/(2*a1))+S-V0*t0)/VF + t0
#     t2_pass=(-V0-(V0**2-2*a1*(V0*t0-S-L))**0.5)/a1+t0

#     T31=(VF-V0)/a1+(H+L+S-V0*t0-(VF**2-V0**2)/2*a1)/VF+t0
#     t31_pass=2*(S-V0*t0)/(VF+V0)+L/VF+t0

#     T32=(2*(S-V0*t0))/(VF+V0)+(H+L)/VF+t0
#     t32_pass=(VF-V0)/a1+(L+S-V0*t0-(VF**2-V0**2)/(2*a1))/VF+t0

#     T_out=max(T31,T2,T32)
#     T_pass_out=max(t2_pass,t31_pass,t32_pass)
#     # if T1==T_out:
#     #     char='T1'
#     if T2==T_out:
#         char='T2'
#     elif T31==T_out:
#         char='T31'   
#     else :
#         char='T32'
#     print(char,'=',T_out,V0,S,a1,t0,V0**2-2*a1*(V0*t0-S-L))
#     T_counter.append(T_out)
#     t_counter.append(T_pass_out)
#     return char,T_out,T_pass_out

# # plot the curve 
# def plot_Time_curve(CT,S_arry,V0_arry,NT2,NT31,NT32):

#     for CT1 in CT:
#         n=0
#         for S in S_arry:
#             T_arry = []
#             n=n+1
#             for V0 in V0_arry:
#                 if CT1:
#                     a1,t0=a1t0withCT(V0)
#                 else:
#                     a1,t0=a1t0withoutCT(V0)
                
                
#                 char,T,t=T_time(V0,8.33,a1,t0,S,L,Hzhi)

#                 if char=='T2':
#                     NT2+=1
#                 if char=='T31':
#                     NT31+=1
#                 if char=='T32':
#                     NT32+=1
#                 T_arry.append(T)        

#             if CT1==1:
#                 print('1')
#                 plt.xlabel('V0 (m/s)')
#                 plt.ylabel('T (s)')
#                 plt.plot(V0_arry, T_arry, label=f'S = {S}')
#                 if n==5:
#                     plt.title(f'直行且有读秒情况下，不同S下的黄灯时间曲线 (S ={S-4}-{S})')
#                     plt.legend()
#                     plt.grid(True)
#                     # plt.show()
#                     plt.savefig(f'{save_path}/Time_Curve_S_WCT_STR{S:.2f}.jpg')
#                     plt.close() 
#                     n=0
#             if CT1==0:
#                 print('1')
#                 plt.xlabel('V0 (m/s)')
#                 plt.ylabel('T (s)')
#                 plt.plot(V0_arry, T_arry, label=f'S = {S}')
#                 if n==5:
#                     plt.title(f'直行且无读秒情况下，不同S下的黄灯时间曲线 (S ={S-4}-{S})')            
#                     plt.legend()
#                     plt.grid(True)
#                     # plt.show()
#                     plt.savefig(f'{save_path}/Time_Curve_S_WOCT_STR{S:.2f}.jpg')
#                     plt.close() 
#                     n=0
#         for V0 in V0_arry:
#             T_arry = []
#             n=n+1
#             for S in S_arry:
#                 if CT1:
#                     a1,t0=a1t0withCT(V0)
#                 else:
#                     a1,t0=a1t0withoutCT(V0)
                
#                 char,T,t=T_time(V0,8.33,a1,t0,S,L,Hzhi)

#                 # print(char,'=',T)
#                 if char=='T2':
#                     NT2+=1
#                 if char=='T31':
#                     NT31+=1
#                 if char=='T32':
#                     NT32+=1
#                 T_arry.append(T)        

#             if CT1==1:
#                 print('1')
#                 plt.xlabel('S(m)')
#                 plt.ylabel('T (s)')
#                 plt.plot(S_arry, T_arry, label=f'V = {V0}')
#                 if n==4:
#                     plt.title(f'直行且有读秒情况下，不同V0下的黄灯时间曲线 (V0 ={V0-3}-{V0})')
#                     plt.legend()
#                     plt.grid(True)
#                     # plt.show()
#                     plt.savefig(f'{save_path}/Time_Curve_V0_WCT_STR{V0}.jpg')
#                     plt.close() 
#                     n=0
#             if CT1==0:
#                 print('1')
#                 plt.xlabel('S(m)')
#                 plt.ylabel('T (s)')
#                 plt.plot(S_arry, T_arry, label=f'S = {V0}')
#                 if n==4:
#                     plt.title(f'直行且无读秒情况下，不同V0下的黄灯时间曲线 (V0 ={V0-3}-{V0})')
#                     plt.legend()
#                     plt.grid(True)
#                     # plt.show()
#                     plt.savefig(f'{save_path}/Time_Curve_V0_WOCT_STR{V0}.jpg')
#                     plt.close() 
#                     n=0

#     # for CT2 in CT:
#     #     n=0
#     #     for S in S_arry:
#     #         T_arry = []
#     #         n=n+1
#     #         for V0 in V0_arry:
#     #             if CT2:
#     #                 a1,t0=a1t0withCT(V0)
#     #             else:
#     #                 a1,t0=a1t0withoutCT(V0)
                
                
#     #             char,T,t=T_time(V0,8.33,a1,t0,S,L,Hwan)

#     #             if char=='T2':
#     #                 NT2+=1
#     #             if char=='T31':
#     #                 NT31+=1
#     #             if char=='T32':
#     #                 NT32+=1
#     #             T_arry.append(T)        

#     #         if CT2==1:
#     #             print('1')
#     #             plt.xlabel('V0 (m/s)')
#     #             plt.ylabel('T (s)')
#     #             plt.plot(V0_arry, T_arry, label=f'S = {S}')
#     #             if n==5:
#     #                 plt.title(f'转弯且有读秒情况下，不同S下的黄灯时间曲线 (S ={S-4}-{S})')
#     #                 plt.legend()
#     #                 plt.grid(True)
#     #                 # plt.show()
#     #                 plt.savefig(f'{save_path}/Time_Curve_S_WCT_Turn{S:.2f}.jpg')
#     #                 plt.close() 
#     #                 n=0
#     #         if CT2==0:
#     #             print('1')
#     #             plt.xlabel('V0 (m/s)')
#     #             plt.ylabel('T (s)')
#     #             plt.plot(V0_arry, T_arry, label=f'S = {S}')
#     #             if n==5:
#     #                 plt.title(f'转弯且无读秒情况下，不同S下的黄灯时间曲线 (S ={S-4}-{S})')            
#     #                 plt.legend()
#     #                 plt.grid(True)
#     #                 # plt.show()
#     #                 plt.savefig(f'{save_path}/Time_Curve_S_WOCT_Turn{S:.2f}.jpg')
#     #                 plt.close() 
#     #                 n=0
#     #     for V0 in V0_arry:
#             # T_arry = []
#             # n=n+1
#             # for S in S_arry:
#             #     if CT2:
#             #         a1,t0=a1t0withCT(V0)
#             #     else:
#             #         a1,t0=a1t0withoutCT(V0)
                
#             #     char,T,t=T_time(V0,8.33,a1,t0,S,L,Hwan)

#             #     # print(char,'=',T)
#             #     if char=='T2':
#             #         NT2+=1
#             #     if char=='T31':
#             #         NT31+=1
#             #     if char=='T32':
#             #         NT32+=1
#             #     T_arry.append(T)        

#             # if CT2==1:
#             #     print('1')
#             #     plt.xlabel('S(m)')
#             #     plt.ylabel('T (s)')
#             #     plt.plot(S_arry, T_arry, label=f'V = {V0}')
#             #     if n==4:
#             #         plt.title(f'转弯且有读秒情况下，不同V0下的黄灯时间曲线 (V0 ={V0-3}-{V0})')
#             #         plt.legend()
#             #         plt.grid(True)
#             #         # plt.show()
#             #         plt.savefig(f'{save_path}/Time_Curve_V0_WCT_Turn{V0}.jpg')
#             #         plt.close() 
#             #         n=0
#             # if CT2==0:
#             #     print('1')
#             #     plt.xlabel('S(m)')
#             #     plt.ylabel('T (s)')
#             #     plt.plot(S_arry, T_arry, label=f'S = {V0}')
#             #     if n==4:
#             #         plt.title(f'转弯且无读秒情况下，不同V0下的黄灯时间曲线 (V0 ={V0-3}-{V0})')
#             #         plt.legend()
#             #         plt.grid(True)
#             #         # plt.show()
#             #         plt.savefig(f'{save_path}/Time_Curve_V0_WOCT_Turn{V0}.jpg')
#             #         plt.close() 
#             #         n=0

# def P(T_counter,t_counter,t):
#     T_number=sum(1 for item in T_counter if item > t)
#     T_percentage=T_number/len(T_counter)
#     t_number=sum(1 for item in t_counter if item > t)
#     t_percentage=t_number/len(t_counter)

#     return T_percentage,t_percentage




# save_path
# plot_Time_curve(CT,S_arry,V0_arry,NT2,NT31,NT32)
# print(NT2,NT31,NT32)

# T_percentage,t_percentage=P(T_counter,t_counter,6)
# print(T_percentage,t_percentage)
# print(len(T_counter),len(t_counter))
# # print(T_counter,t_counter)
