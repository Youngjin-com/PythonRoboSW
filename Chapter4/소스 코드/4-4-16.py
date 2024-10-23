from roboid import *

hamster = Hamster()

while True:
    diff = hamster.left_floor() - hamster.right_floor()
    hamster.wheels(30 + diff * 0.4, 30 - diff * 0.4)

    wait(10) # 너무 빨리 반복하지 않도록 한다.