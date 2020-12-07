# -*- coding: utf-8 -*-

# 1

"""
定义一个 prime() 函数求整数 n 以内（不包括 n）的所有素数（1 不是素数），并返回一个按照升序排列的素数列表。

使用递归来实现一个二分查找算法函数 bi_search()，该函数实现检索任意一个整数在 prime() 函数生成的素数列表中位置（索引）的功能，并返回该位置的索引值，若该数不存在则返回 -1。

输入格式:
  第一行为正整数n
  接下来若干行为待查找的数字，每行输入一个数字

输出格式：
  每行输出相应的待查找数字的索引值

输入样例：
  1
  0
  2
  4
  6
  7

输出样例：
  0
  -1
  -1
  3
  2.
"""

# 2

"""
帕斯卡三角形，又称杨辉三角形是二项式系数在三角形中的一种几何排列。帕斯卡三角形通常从第0行开始枚举，并且每一行的数字是上一行相邻两个数字的和。在第0行只写一个数字1，然后构造下一行的元素。将上一行中数字左侧上方和右侧上方的数值相加。如果左侧上方或者右侧上方的数字不存在，用0替代。下面给出6行的帕斯卡三角形：
       1
      1  1
     1  2  1
    1  3  3  1
   1  4  6  4  1
1  5  10  10  5  1

编写程序，输入帕斯卡三角形的高度n，然后生成和上面例子一样风格的三角形。
"""
