#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyecharts import Pie

pie = Pie('各类电影中"好片"所占的比例', "数据来着豆瓣", title_pos='center')
pie.add("", ["剧情", ""], [25, 75], center=[10, 30], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None, )
pie.add("", ["奇幻", ""], [24, 76], center=[30, 30], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None, legend_pos='left')
pie.add("", ["爱情", ""], [14, 86], center=[50, 30], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)
pie.add("", ["惊悚", ""], [11, 89], center=[70, 30], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)
pie.add("", ["冒险", ""], [27, 73], center=[90, 30], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)
pie.add("", ["动作", ""], [15, 85], center=[10, 70], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)
pie.add("", ["喜剧", ""], [54, 46], center=[30, 70], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)
pie.add("", ["科幻", ""], [26, 74], center=[50, 70], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)
pie.add("", ["悬疑", ""], [25, 75], center=[70, 70], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)
pie.add("", ["犯罪", ""], [28, 72], center=[90, 70], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None, is_legend_show=True, legend_top="center")
pie.show_config()
pie.render()
