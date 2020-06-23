# author: =.= time:2020/6/18
import turtle as t


def koch(size, n):
    if n == 0:
        t.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            t.left(angle)
            koch(size/3, n-1)


def main():
    t.delay(0)
    t.setup(800, 600)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.pensize(2)
    level = 3
    koch(400, level)
    t.left(240)
    koch(400, level)
    t.left(240)
    koch(400, level)
    t.hideturtle()
    t.done()


main()
