from roboid import *

hamster = Hamster()
while True:
    while hamster.left_proximity() < 40 and hamster.right_proximity() < 40:
        hamster.wheels(30, 30)
        wait(20) # 너무 빨리 반복하지 않도록 한다.
    hamster.stop()
    wait(2000)
    hamster.wheels(30, 30)
