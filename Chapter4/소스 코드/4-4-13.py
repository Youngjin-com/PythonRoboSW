from roboid import *

hamster = Hamster()

while True:
    if hamster.left_floor() > 50:
        hamster.wheels(0, 30)
    else:
        hamster.wheels(30, 0)

    wait(10) # 너무 빨리 반복하지 않도록 한다.