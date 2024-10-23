from roboid import *

hamster = Hamster()

while True:
    print(hamster.left_floor(), hamster.right_floor())
    wait(20) # 너무 빨리 반복하지 않도록 한다.
