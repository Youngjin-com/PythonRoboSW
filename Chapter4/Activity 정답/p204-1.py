from roboid import *

hamster = Hamster()
for i in range(4):
    while hamster.left_proximity() < 40 and hamster.right_proximity() < 40:
        hamster.board_forward()
    hamster.board_right()
