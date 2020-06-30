# author: =.= time:2020/6/27
#https://matplotlib.org/gallery/index.html  matplotlib基础源代码
#条形图源代码
# import matplotlib.pyplot as plt
# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 35, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]
# men_std = [2, 3, 4, 1, 2]
# women_std = [3, 5, 2, 3, 3]
# width = 0.35       # the width of the bars: can also be len(x) sequence
# fig, ax = plt.subplots()
# ax.bar(labels, men_means, width, yerr=men_std, label='Men')
# ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
#        label='Women')
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.legend()
# plt.show()



#绘制sin(x)及cos(x^2)的图像
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
# z = np.cos(x**2)
# plt.plot(x, y, "r-", label="$sin(x)$")
# plt.plot(x, z, "b--", label="$cos(x^2)$")
# plt.xlabel("Time(s)") #设置x轴文字
# plt.ylabel("Volt") #设置y轴文字
# plt.title("PyPlot First Example") #设置图表标题
# plt.ylim(-1.2, 1.2) #设置y轴范围
# plt.legend() #图例图示
# plt.show()



#pyplot的绘图区域示例
# import matplotlib.pyplot as plt
# plt.subplot(2, 1, 1)#2行1列，位于区域1
# plt.xticks([]), plt.yticks([])#x轴y轴标号为空
# plt.text(0.5, 0.5,
#          'subplot(2,1,1)', ha='center', va='center', size=24, alpha=.5)
#          #将'subplot(2,1,1)'居中输出，尺寸24，透明度为5
# plt.subplot(2, 1, 2)
# plt.xticks([]), plt.yticks([])
# plt.text(0.5, 0.5,
#          'subplot(2,1,2)', ha='center', va='center', size=24, alpha=.5)
# plt.show()



#折线图示例
# import matplotlib.pyplot as plt
# data = [1, 2, 3, 6, 4, 2, 7]
# plt.plot(data, color="c", linestyle=":") #第一个参数表示横坐标数据，第二个参数为纵坐标，第三个参数表示颜色、线性、标记样式
# plt.show()  #颜色有r/g/b/c/m/y/k/w 线型有-/--/：/-.
#             # 标记样式有./,/o/v/^/s/*/D/d/x/</>/h/H/1/2/3/4/_/|



#绘制多条曲线、曲线颜色、线型、标记等参数设置
# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
# xx = [3, 4, 5, 1, 9, 3, 2, 5, 6, 3]
# yy = [1, 2, 3, 4, 5, 3, 1, 2, 7, 8]
# zz = [2, 2, 4, 7, 4, 8, 2, 4, 5, 6]
# plt.plot(xx, color="k", linestyle="-.", label="Data 1")
# plt.plot(yy, color="m", linestyle=":", label="Data 2")
# plt.plot(zz, color="y", linestyle="--", label="Data 3")
# plt.legend()
# plt.xlabel("x轴", fontproperties="simhei")
# plt.ylabel("y轴", fontproperties="simhei")
# plt.title("折线图进阶", fontproperties="simhei")
# plt.show()



#折线图练习
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] #改进 x = list(range(1, 13))
y = [5.2, 7.7, 5.8, 5.7, 7.3, 9.2, 18.7, 14.6, 20.5, 17.0, 9.8, 6.9]
plt.xlabel("月份", fontproperties="simhei", fontsize=14)
plt.ylabel("营业额(万元)", fontproperties="simhei", fontsize=14)
plt.title("19年营业额", fontproperties="simhei", fontsize=18)
plt.plot(x, y, 'r-.v')
plt.legend()
plt.show()



#散点图的方法
#matplotlib.pyplot.scatter(x, y , s=None, c=None, marker=None, cmap=None,
# norm=None, vmin=None, vmax=None, alpha=None, linewideths=None, verts=None,
# edgecolors=None, hold=None, data=None, **kwargs)
#x,y组成了散点的坐标;s为散点的面积;c为散点的颜色(默认为蓝色'b');marker为散点的标记；
#alpha为散点的透明度(0与1之间的数,0为完全透明.1为完全不透明)；linewidths为散点边缘的线度；
#如果marker为None,则使用verts的值构建散点标记；edgecolors为散点的边缘颜色
#绘制普通散点图示例
# import matplotlib.pyplot as plt
# import numpy as np
# N = 10
# x = np.random.rand(N)
# y = np.random.rand(N)
# size = (30 * np.random.rand(N))**2#改变随机点的大小
# color = np.random.rand(N)#改变随机点的颜色
# plt.scatter(x, y, size, c=color, alpha=0.5, marker='^')#alpha透明度为0.5，marker改变随机点的形状为三角形
# plt.show()