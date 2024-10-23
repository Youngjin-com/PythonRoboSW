from roboid import *

hamster = Hamster()
while hamster.left_proximity() < 40 and hamster.right_proximity() < 40:
    hamster.board_forward()
hamster.board_left()
