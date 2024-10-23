import turtle
from roboid import *

turtle.shape('turtle')

hamster = Hamster()

while True:
    x = -round(hamster.acceleration_y() / 1500.0) * 30
    y = -round(hamster.acceleration_x() / 1500.0) * 30

    turtle.goto(x, y)

    wait(20) # 너무 빨리 반복하지 않도록 한다.
