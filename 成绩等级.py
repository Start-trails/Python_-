# author: =.= time:2020/5/21
score = eval(input("请输入你的成绩:"))
if score in range(90, 101):
    print("A")
elif score in range(80, 90):
    print("B")
elif score in range(70, 80):
    print("C")
elif score in range(60, 70):
    print("D")
else:
    print("不及格")

