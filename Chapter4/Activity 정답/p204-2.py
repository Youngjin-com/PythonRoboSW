from roboid import *

hamster = Hamster()
while hamster.left_proximity() < 40 and hamster.right_proximity() < 40:
    hamster.board_forward()
hamster.board_right()
hamster.board_right()
for i in range(2):
    while hamster.left_proximity() < 40 and hamster.right_proximity() < 40:
        hamster.board_forward()
    hamster.board_right()
