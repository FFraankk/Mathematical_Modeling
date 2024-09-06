# import matplotlib.pyplot as plt
# import numpy as np

# # 定义螺旋线的参数
# a = 1.0  # 螺旋线的起始半径
# b = 55 / (2 * np.pi)  # 螺旋线的增长速率，这里假设每圈的长度是55 cm
# n_turns = 16  # 圈数
# resolution = 1000  # 每圈的采样点数量

# # 创建角度数组
# theta = np.linspace(0, n_turns * 2 * np.pi, resolution * n_turns)

# # 计算螺旋线上点的坐标
# r = a + b * theta
# x = r * np.cos(theta)
# y = r * np.sin(theta)

# # 绘制螺旋线
# plt.figure(figsize=(8, 8))
# plt.plot(x, y, lw=0.5)
# plt.axhline(0, color='black',linewidth=0.5)
# plt.axvline(0, color='black',linewidth=0.5)

# # 设置轴标签和标题
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Clockwise Archimedean Spiral')

# # 显示图形
# plt.show()


from scipy.optimize import fsolve
import numpy as np

# 定义方程
def equation(x):
    return 880*880 + (880 - x*55/6.28)**2 - 2*880*(880 - x*55/6.28)*np.cos(x) - 286*286

# 使用fsolve求解方程，提供一个初始猜测值
initial_guess = 0
solution = fsolve(equation, initial_guess)

print(solution)

# print(np.cos(solution[0])*286/((880-solution[0]*55/6.28)*np.sin(solution[0])))

# import numpy as np
# from scipy.integrate import quad
# from scipy.optimize import root_scalar

# # 定义函数 f(x)
# def f(x):
#     return x**2  # 示例函数

# # 已知积分结果 I(a, b) 和下界 a
# I_known = 1.0  # 假设已知积分结果为 1.0
# a = 0  # 下界为 0

# # 定义方程，用于找到上界 b
# def equation(b):
#     I_calculated, _ = quad(f, a, b)
#     return I_calculated - I_known

# # 使用 root_scalar 寻找 b
# result = root_scalar(equation, bracket=[a, 10], method='brentq')

# if result.converged:
#     b_upper = result.root
#     print(f"上界 b = {b_upper}")
# else:
#     print("未找到解")
