import numpy as np
from sympy import symbols, integrate, sqrt
from scipy.optimize import root,brentq
import matplotlib.pyplot as plt
import pandas as pd
from sympy import symbols, Eq, solve, sqrt, cos, S, Interval,solveset

for chouxiang in range(60,62):

    b = chouxiang/(2*np.pi)

    theta = symbols('theta')

    # 定义被积函数
    f = sqrt(b**2 * theta**2 + b**2)

    # 计算积分
    Total_Length = integrate(f, (theta, 0, 32*np.pi))

    def r_length(theta):
        return 880-b * theta

    def positionX(theta):
        return (b*(32*np.pi-theta)*np.cos(32*np.pi-theta))/100

    def positionY(theta):
        return (b*(32*np.pi-theta)*np.sin(32*np.pi-theta))/100


    L1 = 341-27.5*2
    L2 = 220-27.5*2
    V0 = 100

    def equation(x, V0, t):
        return 0.5 * x * np.sqrt(1 + x**2) + 0.5 * np.log(np.abs(x + np.sqrt(1 + x**2))) - (float(Total_Length) - V0 * t) / b


    # 龙头对应时间的角度
    solutions = []

    # 对每个t值求解方程
    # for t_value in range(301):
    for t_value in range(444):
        result_head_theta = root(equation, 1, args=(V0, t_value)) 
        if result_head_theta.success:
            solutions.append(result_head_theta.x[0])
        else:
            solutions.append(None)  # 如果没有找到解，则存储None
        


    theta_rad = 32 * np.pi - np.array(solutions)
    mei_miao_long_tou_de_theta=theta_rad.tolist()  #龙头对应时间的角度
    # print(mei_miao_long_tou_de_theta)
    # x=positionX(theta_rad)
    # y=positionY(theta_rad)
    # plt.plot(x,y)

    # 两点间距离判断公式
    def eq_others(x,theta):
        return sqrt(r_length(theta)**2 + r_length(x)**2 - 2 * r_length(theta) * r_length(x) * np.cos(theta - x)) - L2


    def eq_head(x,theta_temp,L1):
        return np.sqrt(r_length(theta_temp)**2 + r_length(x)**2 - 2 * r_length(theta_temp) * r_length(x) * np.cos(theta_temp - x)) - L1

    # 返回某个时刻，某个把手的theta 值
    # body_theta是返回的把手的前一个的theta值
    def longshenliebiaodetheta(body_theta):
        step=0.01
        panduan=True
        theta_Loong=[]
        theta_Loong.append(body_theta)
        

        while panduan:
            
            theta_Loong_new_element=theta_Loong[-1]-step

            if np.abs(eq_others(body_theta,theta_Loong_new_element))<0.01:
                panduan = False
                return theta_Loong_new_element
            elif round(eq_others(body_theta,theta_Loong[-1]),3) * round(eq_others(body_theta,theta_Loong_new_element),3) < 0:
                panduan = False
                return (theta_Loong_new_element+theta_Loong[-1])/2
            else:
                theta_Loong.append(theta_Loong_new_element)



    table1=[]
    table_posxy=[]
    v_pos=[]
    # for time in range(301):
    for time in range(442):
        # print(time)
        solutions_row=[]
        solutionsXY_row=[]

        v_row=[]

        theta_temp = mei_miao_long_tou_de_theta[time] 
        
        solutions_row.append(theta_temp)
        solutionsXY_row.append(positionX(theta_temp))
        solutionsXY_row.append(positionY(theta_temp))
        v_row.append(1)

        result_head = root(eq_head, theta_temp-1, args=(theta_temp, L1)) 
        solutions_row.append(result_head.x[0])


        solutionsXY_row.append(positionX(result_head.x[0]))
        solutionsXY_row.append(positionY(result_head.x[0]))
        v_row.append(r_length(solutions_row[1])/r_length(solutions_row[0]))

        for i in range(18):
            
            # 现在的把手的位置是solutions_row[i+1]
            # 这个循环开始求解下一个角度
            bbb = longshenliebiaodetheta(solutions_row[i+1])
            # print(bbb)
            solutions_row.append(bbb)
            solutionsXY_row.append(positionX(bbb))
            solutionsXY_row.append(positionY(bbb))

            v_row.append(r_length(solutions_row[i+2])/r_length(solutions_row[0]))
        # print(v_row)
        # print(solutions_row)
        table1.append(solutions_row)
        table_posxy.append(solutionsXY_row)
        v_pos.append(v_row)
        

    # 统一用 米制
    # 任意两点的直线方程
    c = chouxiang/(2*np.pi)
    def positionX1(theta):
        return (c*(32*np.pi-theta)*np.cos(32*np.pi-theta))/100

    def positionY1(theta):
        return (c*(32*np.pi-theta)*np.sin(32*np.pi-theta))/100

    def line_equation_center(theta1,theta2):
        x1=positionX1(theta1)
        y1=positionY1(theta1)
        x2=positionX1(theta2)
        y2=positionY1(theta2)
    # 孔的直线方程
        k_center=(y2-y1)/(x2-x1) 
        b_center=y1-k_center*x1 
        # print(theta1,theta2,x1,y1,x2,y2,k_center,b_center)
        return k_center,b_center

    # 在已知中心直线的情况下，求龙头的靠外的直线方程
    def line_equation_out(k,bp):
        b1=bp+0.15*np.sqrt(1+k**2)
        b2=bp-0.15*np.sqrt(1+k**2)

        if b1<b2:
            b_out=b1
        else:
            b_out=b2
        k_out=k
        return k_out,b_out

    def distance(theta_head,k_out,b_out,k,b):
        x0=positionX1(theta_head)
        y0=positionY1(theta_head)
        delta= (2*k*(b_out-y0)-2*x0)**2-4*(k_out**2+1)*(x0**2+y0**2-2*y0*b_out+b_out**2-157/1600)
        # print(delta)
        m1=(2*x0-2*k*(b_out-y0)+np.sqrt(delta))/(2*(k_out**2+1))
        m2=(2*x0-2*k*(b_out-y0)-np.sqrt(delta))/(2*(k_out**2+1))
        n1=k_out*m1+b_out
        n2=k_out*m2+b_out

        
        A = -k
        B = 1
        C = -b

        dis1=abs(A *m1+ B *n1+ C) / np.sqrt(A**2 + B**2)
        dis2=abs(A *m2 + B * n2 + C) / np.sqrt(A**2 + B**2)
        return dis1,dis2

    break_bool=False
    final_time=0
    for time in range(380,442):
        # 这里找到在这个时刻，龙头的相关信息

        k_head_center,b_head_center=line_equation_center(table1[time][0],table1[time][1])
        k_head_out,b_head_out=line_equation_out(k_head_center,b_head_center)
        # print(time)
        for loong in range(1,16):
    
        # 龙头的把手是第0个把手，身子的把手是第1个把手
        # 龙头是loong-1
            k_body_center,b_body_center=line_equation_center(table1[time][loong],table1[time][loong+1])
            dis1,dis2=distance(table1[time][0],k_head_out,b_head_out,k_body_center,b_body_center)

            if dis1<=0.15:
                break_bool=True
                final_time=time
                final_boom=loong
                break
            if dis2<=0.15:
                break_bool=True
                final_time=time
                final_boom=loong
                break
        if break_bool:
            break
    r=sqrt(positionX1(table1[final_time][0])**2+positionY1(table1[final_time][0])**2)

    print(final_time,final_boom,r,chouxiang)

