import turtle
from roboid import *

turtle.shape('turtle')

hamster = Hamster()

while True:
    y = -round(hamster.acceleration_x() / 1500.0) * 30

    turtle.goto(0, y)

    wait(20) # 너무 빨리 반복하지 않도록 한다.
