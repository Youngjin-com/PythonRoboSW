from roboid import *

hamster = Hamster()

while True:
    hamster.wheels(30, 30)
    if hamster.left_floor() < 50:
        hamster.wheels(-30, 30)
    elif hamster.right_floor() < 50:
        hamster.wheels(30, -30)

    wait(10) # 너무 빨리 반복하지 않도록 한다.