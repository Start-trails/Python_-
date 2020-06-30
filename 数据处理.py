# author: =.= time:2020/6/19
# numpy提供ndarray，ndarray是存储单一数据类型的多维数组
# ndarray中的每个元素在内存中都有相同存储大小区域
# ndarray中每个元素是数据类型对象的对象（称为 dtype）
# 可以通过对数组进行索引或切片
# 可通过ndarray的方法和属性来访问和修改ndarray的内容
# import random
#
# def genpwd(length):
#     a = 10**(length-1)
#     b = 10**length - 1
#     return "{}".format(random.randint(a, b))
#
# length = eval(input())
# random.seed(17)
# for i in range(3):
#     print(genpwd(length))


# N = input()
# s = 0
# m = {}
# for i in N:
#     m[i] = m.get(i,0)+1
# word = list(m.keys())
# for i in word:
#     i = int(i)
#     s += i
# print(s)


