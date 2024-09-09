import numpy as np
from sympy import symbols, integrate, sqrt
from scipy.optimize import root
import pandas as pd


# 螺距比例
b = 170/(2*np.pi)

theta = symbols('theta')

# 定义被积函数
f = sqrt(b**2 * theta**2 + b**2)

# 计算积分
Total_Length = integrate(f, (theta, 0, 32*np.pi))

def r_length(theta):
    return 880-b * theta

# 坐标转换方程
def positionX(theta):
    return (b*(32*np.pi-theta)*np.cos(32*np.pi-theta))/100

def positionY(theta):
    return (b*(32*np.pi-theta)*np.sin(32*np.pi-theta))/100

# 两个孔距
L1 = 341-27.5*2
L2 = 220-27.5*2
# 龙头的速度
V0 = 100

def equation(x, V0, t):
    return 0.5 * x * np.sqrt(1 + x**2) + 0.5 * np.log(np.abs(x + np.sqrt(1 + x**2))) - (float(Total_Length) - V0 * t) / b


# 龙头对应时间的角度
solutions = []

# 找每个时刻头对应的角度，从里往外
for t_value in range(442):
# for t_value in range(1510):
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

# 龙头专用距离判断公式，root（）备用
def eq_head(x,theta_temp,L1):
    return np.sqrt(r_length(theta_temp)**2 + r_length(x)**2 - 2 * r_length(theta_temp) * r_length(x) * np.cos(theta_temp - x)) - L1

# 返回某个时刻，某个把手的theta 值
# body_theta是返回的把手的前一个的theta值
def longshenliebiaodetheta(body_theta):
    step=0.05
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

# 存储每个时刻，每个把手的角度
table1=[]
# 存储每个时刻，每个把手在笛卡尔坐标系下的位置
table_posxy=[]
# 存储每个时刻，每个把手在笛卡尔坐标系下的速度
v_pos=[]
for time in range(301):
# for time in range(442):
    print(time)
    solutions_row=[]
    solutionsXY_row=[]

    v_row=[]

    theta_temp = mei_miao_long_tou_de_theta[time] 
    # 龙头信息写入
    solutions_row.append(theta_temp)
    solutionsXY_row.append(positionX(theta_temp))
    solutionsXY_row.append(positionY(theta_temp))
    v_row.append(1)

    result_head = root(eq_head, theta_temp-1, args=(theta_temp, L1)) 
    solutions_row.append(result_head.x[0])

    # 第一个龙神把手信息写入
    solutionsXY_row.append(positionX(result_head.x[0]))
    solutionsXY_row.append(positionY(result_head.x[0]))
    v_row.append(r_length(solutions_row[1])/r_length(solutions_row[0]))

    for i in range(222):
        
        # 现在的把手的位置是solutions_row[i+1]
        # 这个循环开始求解下一个角度
        bbb = longshenliebiaodetheta(solutions_row[i+1])
        # print(bbb)

        # 从第二个龙身开始，信息逐个写入
        solutions_row.append(bbb)
        solutionsXY_row.append(positionX(bbb))
        solutionsXY_row.append(positionY(bbb))

        v_row.append(r_length(solutions_row[i+2])/r_length(solutions_row[0]))
    # print(v_row)
    # print(solutions_row)
    # 逐行写入总表
    table1.append(solutions_row)
    table_posxy.append(solutionsXY_row)
    v_pos.append(v_row)


# 统一保存
# 列表转化到result中要求的格式
table1_final = np.round(np.transpose(table_posxy),6)
v_pos_final = np.round(np.transpose(v_pos),6)
df1 = pd.DataFrame(table1_final)
df2 = pd.DataFrame(v_pos_final)

file1_path = r'D:\Mathematical_Modeling\MCM2024\CUMCM2024Problems\A题\Solution\result1逼近位置.xlsx'
df1.to_excel(file1_path, index=False, header=False)
file2_path = r'D:\Mathematical_Modeling\MCM2024\CUMCM2024Problems\A题\Solution\result1逼近速度.xlsx'
df2.to_excel(file2_path, index=False, header=False)
df3 = pd.DataFrame(table1)
file3_path = r'D:\Mathematical_Modeling\MCM2024\CUMCM2024Problems\A题\Solution\question1角度.xlsx'
df3.to_excel(file3_path, index=False, header=False)