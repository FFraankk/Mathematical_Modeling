# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # 读取Excel文件
# df = pd.read_excel(r'D:\Mathematical_Modeling\MCM2024\CUMCM2024Problems\A题\Solution\步长0001.xlsx')

# # # 获取第一列的数据作为y轴数据
# # y_data = df.iloc[:, 0]

# # # 生成x轴数据，长度与y轴数据相同，从0开始
# # x_data = np.arange(len(y_data))


# # plt.rcParams['font.sans-serif'] = ['SimHei'] 
# # plt.rcParams['axes.unicode_minus'] = False 

# # # 绘制图表
# # plt.plot(x_data, y_data,)
# # plt.xlabel('时间')
# # plt.ylabel('龙头对应的theta值')
# # plt.title('龙头对应的theta值和时间的关系')
# # plt.show()



# # # 获取第一列的数据作为y轴数据
# # y_data = df.iloc[280, :]

# # # 生成x轴数据，长度与y轴数据相同，从0开始
# # x_data = np.arange(len(y_data))


# # plt.rcParams['font.sans-serif'] = ['SimHei'] 
# # plt.rcParams['axes.unicode_minus'] = False 

# # # 绘制图表
# # plt.plot(x_data, y_data,)
# # plt.xlabel('把手序号')
# # plt.ylabel('各个把手对应的theta值')
# # plt.title('280秒时各个把手对应的theta值与把手序号的关系')
# # plt.show()



# # import matplotlib.pyplot as plt
# # from math import cos, sin, pi

# # def draw_spiral():
# #     # 设置画布大小
# #     fig = plt.figure(figsize=(8, 8))
    
# #     # 创建子图
# #     ax = fig.add_subplot(111)
    
# #     # 定义螺旋线的参数
# #     num_turns = 10  # 螺旋线旋转圈数
# #     points_per_turn = 1000  # 每圈的点数
    
# #     # 初始化坐标列表
# #     x_coords = []
# #     y_coords = []
    
# #     for i in range(num_turns * points_per_turn):
# #         angle = i / points_per_turn * 2 * pi  # 计算角度
# #         radius = i / (num_turns * points_per_turn)  # 计算半径
        
# #         x = radius * cos(angle)  # 计算x坐标
# #         y = radius * sin(angle)  # 计算y坐标
        
# #         x_coords.append(x)
# #         y_coords.append(y)
        
# #         if i % points_per_turn == 0:
# #             # 绘制小方块
# #             ax.plot([x], [y], 'ro', markersize=5)
            
# #     # 绘制螺旋线
# #     ax.plot(x_coords, y_coords, color='r')
    
# #     # 隐藏边框
# #     ax.spines['top'].set_visible(False)
# #     ax.spines['right'].set_visible(False)
# #     ax.spines['left'].set_visible(False)
# #     ax.spines['bottom'].set_visible(False)
    
# #     # 移动轴心到中心
# #     ax.spines['left'].set_position('center')
# #     ax.spines['bottom'].set_position('center')
    
# #     # 设置背景颜色为白色
# #     ax.set_facecolor('white')
    
# #     # 显示图形
# #     plt.show()


# # draw_spiral()

# import matplotlib.pyplot as plt
# import matplotlib.patches as patches

# def draw_connected_rectangles(num_rectangles, width, height):
#     fig, ax = plt.subplots(figsize=(8, 8))
    
#     # 初始化起始位置
#     x_start = 0
#     y_start = 0
    
#     # 绘制矩形
#     for i in range(num_rectangles):
#         # 创建矩形
#         rect = patches.Rectangle(
#             (x_start, y_start),  # 矩形左下角的坐标
#             width,  # 矩形的宽度
#             height,  # 矩形的高度
#             edgecolor='black',
#             facecolor='none'  # 矩形填充颜色为无
#         )
        
#         # 将矩形添加到子图中
#         ax.add_patch(rect)
        
#         # 更新下一个矩形的起始位置
#         x_start += width
        
#         # 为了避免重叠，我们可以添加一些间隔
#         if i % 2 == 0:
#             y_start += height / 2
    
#     # 设置坐标轴范围
#     ax.set_xlim(0, x_start)
#     ax.set_ylim(0, y_start + height / 2)
    
#     # 隐藏坐标轴
#     ax.axis('off')
    
#     # 显示图形
#     plt.show()

# # 调用函数绘制矩形
# draw_connected_rectangles(num_rectangles=10, width=10, height=5)
