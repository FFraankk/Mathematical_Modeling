import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False 

path1 =r'D:\Mathematical_Modeling\training\rate.csv'

df = pd.read_csv(path1)

T = np.array(df['黄灯时长(s)'])
Pass_rate = np.array(df['通过对侧停止线百分比(%)'])/100

coefficients_linear = np.polyfit(T, Pass_rate, 1)
y_pred_linear = np.polyval(coefficients_linear, T)
mse_linear = np.mean((Pass_rate - y_pred_linear) ** 2)

coefficients_quadratic = np.polyfit(T, Pass_rate, 2)
y_pred_quadratic = np.polyval(coefficients_quadratic, T)
mse_quadratic = np.mean((Pass_rate - y_pred_quadratic) ** 2)

coefficients_cubic = np.polyfit(T, Pass_rate, 3)
y_pred_cubic = np.polyval(coefficients_cubic, T)
mse_cubic = np.mean((Pass_rate - y_pred_cubic) ** 2)

print(mse_linear,mse_quadratic,mse_cubic)
print(f'{coefficients_quadratic[0]}x**2+{coefficients_quadratic[1]}x{coefficients_quadratic[2]}')
plt.scatter(T, Pass_rate, label='通过率')
plt.plot(T, y_pred_linear, label='线性拟合')
plt.plot(T, y_pred_quadratic, label='二次多项式拟合')
plt.plot(T, y_pred_cubic, label='三次多项式拟合')
plt.xlabel('T')
plt.ylabel('通过率')
plt.title('通过率和时间的拟合曲线')
plt.legend()
plt.show()

