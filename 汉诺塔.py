# author: =.= time:2020/6/17
# #将字符串s反转后输出
# def rvs(s):
#     if s == "":
#         return s
#     else:
#         return rvs(s[1:])+s[0]
# def main():
#     s = "123456"
#     print(rvs(s))
# main()

# 斐波那契数列
# def f(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return f(n-1) + f(n-2)
#
# def main():
#     for i in range(1, 6):
#         print(f(i))
# main()
#汉诺塔
# count = 0
# def hanoi(n, src, dst, mid):
#     global count
#     if n == 1:
#         print("{}:{}->{}".format(1, src, dst))
#         count += 1
#     else:
#         hanoi(n-1, src, mid, dst)
#         print("{}:{}->{}".format(n, src, dst))
#         count += 1
#         hanoi(n-1, mid, dst, src)
# hanoi(3, 'A', 'C', 'B')
# print(count)