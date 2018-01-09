#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
# 绘图和演示函数分别为：plt.plot() plt.show()
# plot方法可以接受两个变量作为x轴和y轴，对象可以为任何可
# 迭代（iterable）类型，如numpy.array和pandas.Series
# plt.plot(x_values, y_values)
# 当坐标轴的标记显得过于拥挤时，可以通过xticks或yticks方法旋转标记
# plt.xticks(rotation=90)
# xlabel、ylabel和title方法接收一个字符串作为参数传入，
# 将其作为x轴、y轴和图标的标签plt.xlabel(“x”) plt.ylabel(“y”) plt.title(“title”)
# 需要在同一张图绘制两条曲线时，调用两次plot方法即可,
# 参数c、label可以分别指定颜色和标签，legend方法可以绘制图例
# Axes.tick_params方法可以去除轴上的标记
# Spine.set_visible()方法可以去除图表的边框
# subplot方法：绘制子图