# author: =.= time:2020/6/16
#绘制蟒蛇
# import turtle
# turtle.setup(650, 350, 200, 200)
# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize(25)
# # turtle.pencolor("purple")
# turtle.seth(-40)
# for i in range(4):
#     turtle.circle(40, 80)
#     turtle.circle(-40, 80)
# turtle.circle(40, 80/2)
# turtle.fd(40)
# turtle.circle(16, 180)
# turtle.fd(40*2/3)
# turtle.done()

# import turtle
# def drawLine(draw):#绘制单段数码管
#     turtle.pendown() if draw else turtle.penup()
#     turtle.fd(40)
#     turtle.right(90)
# def drawDigit(digit):#根据数字绘制七段数码管
#     drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
#     drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
#     turtle.left(90)
#     drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
#     drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
#     turtle.left(180)
#     turtle.penup()#为绘制后续数字确定位置
#     turtle.fd(20)#为绘制后续数字确定位置
# def drawDate(date):  # date为日期，格式为‘%Y-%m=%d+’
#     for i in date:
#          drawDigit(eval(i))  # 通过eval()函数将数字变为整数
# def main():
#     turtle.setup(800, 350, 200, 200)
#     turtle.penup()
#     turtle.fd(-300)
#     turtle.pensize(5)
#     drawDate('20200628')
#     turtle.hideturtle()
#     turtle.done()
# main()

# 大风车
import turtle as t
t.pensize(2)
for i in range(4):
    if i == 0:
        t.color("red")
    elif i == 1:
        t.color("blue")
    elif i == 2:
        t.color("green")
    elif i == 3:
        t.color("yellow")
    t.seth(90*i)
    t.fd(150)
    t.left(270)
    t.circle(-150, 45)
    t.goto(0, 0)
t.color("purple")
t.left(135)
t.fd(350)
t.done()