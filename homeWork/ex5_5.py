import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.pd
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

t = turtle.Turtle()
draw(t, 10, 2)
input()
