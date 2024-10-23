import turtle
from roboid import *

turtle.shape('turtle') # 거북이를 표시한다.

hamster = Hamster()

while True:
    y = -hamster.acceleration_x() / 50 # 햄스터 로봇의 앞을 위로 들면 X축 가속도 값은 음수이다.

    turtle.goto(0, y)

    wait(20) # 너무 빨리 반복하지 않도록 한다.
